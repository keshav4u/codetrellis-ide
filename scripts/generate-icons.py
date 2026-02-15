#!/usr/bin/env python3
# --------------------------------------------------------------------------------------------
# Copyright (c) Codetrellis Contributors. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
"""
Generate CodeTrellis app icons for all platforms.

Design concept:
  CodeTrellis = "Project Self-Awareness System"
  - A trellis is a lattice structure where things grow and interconnect
  - The icon shows a network of connected nodes (knowledge graph)
  - Central node is larger and brighter (the "awareness" / brain)
  - Surrounding nodes represent code artifacts (schemas, routes, services)
  - Connections between nodes represent relationships CodeTrellis discovers
  - All on a deep navy to teal gradient (developer-tool aesthetic)
  - Rounded-square shape (modern app icon standard)

Produces:
  resources/darwin/code.icns       (macOS)
  resources/linux/code.png         (Linux 512x512)
  resources/win32/code.ico         (Windows multi-size)
  resources/win32/code_150x150.png (Windows tile)
  resources/win32/code_70x70.png   (Windows tile)
  resources/win32/inno-big-*.bmp   (Inno Setup wizard)
  resources/win32/inno-small-*.bmp (Inno Setup header)
"""

import math
import os
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageFilter

# -- Palette ----------------------------------------------------------------
BG_TOP      = (12, 25, 48)       # Very deep navy
BG_MID      = (15, 42, 72)       # Mid navy
BG_BOTTOM   = (8, 90, 100)       # Dark teal

NODE_CORE   = (0, 220, 190)      # Bright cyan-teal  (central node)
NODE_RING   = (0, 180, 160)      # Slightly muted ring around core
NODE_INNER  = (60, 210, 200)     # Inner ring nodes
NODE_OUTER  = (40, 160, 170)     # Outer ring nodes
NODE_GLOW   = (0, 255, 220, 60)  # Glow around nodes

EDGE_BRIGHT = (0, 200, 180, 130) # Bright connection lines
EDGE_DIM    = (0, 160, 150, 60)  # Dimmer outer connections

BRACKET_CLR = (220, 240, 255, 220)  # Subtle white-blue brackets


def lerp(a, b, t):
    return int(a + (b - a) * t)

def lerp_color(c1, c2, t):
    return tuple(lerp(a, b, t) for a, b in zip(c1, c2))


def generate_icon(size):
    """Generate the CodeTrellis icon at a given pixel size."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))

    margin = int(size * 0.06)
    radius = int(size * 0.20)
    cx, cy = size // 2, size // 2

    # -- 1. Background gradient (3-stop: navy > mid > teal) --
    bg = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    for y in range(size):
        t = y / size
        if t < 0.5:
            color = lerp_color(BG_TOP, BG_MID, t * 2)
        else:
            color = lerp_color(BG_MID, BG_BOTTOM, (t - 0.5) * 2)
        for x in range(size):
            bg.putpixel((x, y), (*color, 255))

    mask = Image.new('L', (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=radius, fill=255
    )
    bg.putalpha(mask)
    img = Image.alpha_composite(img, bg)

    # -- 2. Subtle radial glow behind the centre --
    glow = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_r = int(size * 0.32)
    for r in range(glow_r, 0, -1):
        alpha = int(35 * (1 - r / glow_r) ** 2)
        glow_draw.ellipse(
            [cx - r, cy - r, cx + r, cy + r],
            fill=(0, 200, 180, alpha)
        )
    glow.putalpha(Image.composite(glow.split()[3], Image.new('L', (size, size), 0), mask))
    img = Image.alpha_composite(img, glow)

    # -- 3. Trellis lattice (subtle diagonal crosshatch) --
    lattice = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lattice)
    lw = max(1, int(size * 0.007))
    spacing = int(size * 0.065)
    lcolor = (255, 255, 255, 18)

    for offset in range(-size, size * 2, spacing):
        ld.line([(offset, margin), (offset + size, size - margin)], fill=lcolor, width=lw)
        ld.line([(offset + size, margin), (offset, size - margin)], fill=lcolor, width=lw)

    lattice.putalpha(Image.composite(lattice.split()[3], Image.new('L', (size, size), 0), mask))
    img = Image.alpha_composite(img, lattice)

    # -- 4. Node positions (trellis network graph) --
    # Central node + 2 rings of satellite nodes
    s = size  # shorthand

    # Inner ring: 6 nodes around centre
    inner_r = int(s * 0.17)
    inner_nodes = []
    for i in range(6):
        angle = math.radians(i * 60 - 90)
        nx = cx + int(inner_r * math.cos(angle))
        ny = cy + int(inner_r * math.sin(angle))
        inner_nodes.append((nx, ny))

    # Outer ring: 12 nodes further out
    outer_r = int(s * 0.31)
    outer_nodes = []
    for i in range(12):
        angle = math.radians(i * 30 - 75)
        nx = cx + int(outer_r * math.cos(angle))
        ny = cy + int(outer_r * math.sin(angle))
        outer_nodes.append((nx, ny))

    # -- 5. Draw edges (connections) --
    edge_layer = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    ed = ImageDraw.Draw(edge_layer)
    edge_w = max(1, int(s * 0.009))
    thin_w = max(1, int(s * 0.006))

    # Centre to inner nodes
    for (nx, ny) in inner_nodes:
        ed.line([(cx, cy), (nx, ny)], fill=EDGE_BRIGHT, width=edge_w)

    # Inner to adjacent inner (hexagonal ring)
    for i in range(len(inner_nodes)):
        j = (i + 1) % len(inner_nodes)
        ed.line([inner_nodes[i], inner_nodes[j]], fill=EDGE_BRIGHT, width=thin_w)

    # Inner to nearest outer nodes
    for i, (inx, iny) in enumerate(inner_nodes):
        # Each inner connects to 2 nearest outer nodes
        o1 = i * 2
        o2 = i * 2 + 1
        ed.line([(inx, iny), outer_nodes[o1 % 12]], fill=EDGE_DIM, width=thin_w)
        ed.line([(inx, iny), outer_nodes[o2 % 12]], fill=EDGE_DIM, width=thin_w)

    # Some outer-to-outer connections (every other)
    for i in range(0, 12, 2):
        j = (i + 1) % 12
        ed.line([outer_nodes[i], outer_nodes[j]], fill=(0, 140, 130, 35), width=thin_w)

    edge_layer.putalpha(
        Image.composite(edge_layer.split()[3], Image.new('L', (size, size), 0), mask)
    )
    img = Image.alpha_composite(img, edge_layer)

    # -- 6. Draw nodes --
    node_layer = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    nd = ImageDraw.Draw(node_layer)

    def draw_node(x, y, r, color, glow_color=None, glow_r_mult=2.5):
        """Draw a glowing circular node."""
        if glow_color:
            for gr in range(int(r * glow_r_mult), 0, -1):
                alpha = int(glow_color[3] * (1 - gr / (r * glow_r_mult)) ** 1.5)
                nd.ellipse(
                    [x - gr, y - gr, x + gr, y + gr],
                    fill=(*glow_color[:3], alpha)
                )
        nd.ellipse([x - r, y - r, x + r, y + r], fill=(*color, 255))
        # Highlight dot (top-left specular)
        hr = max(1, r // 3)
        hx, hy = x - r // 4, y - r // 4
        nd.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=(255, 255, 255, 90))

    # Outer ring nodes (smallest)
    outer_node_r = max(2, int(s * 0.018))
    for (nx, ny) in outer_nodes:
        draw_node(nx, ny, outer_node_r, NODE_OUTER, (*NODE_OUTER, 30), 2.0)

    # Inner ring nodes (medium)
    inner_node_r = max(3, int(s * 0.028))
    for (nx, ny) in inner_nodes:
        draw_node(nx, ny, inner_node_r, NODE_INNER, (*NODE_INNER, 45), 2.5)

    # Central node (largest, brightest, with prominent glow)
    core_r = max(5, int(s * 0.055))
    draw_node(cx, cy, core_r, NODE_CORE, (*NODE_CORE, 70), 3.5)

    # Inner bright ring on central node
    ring_r = max(3, int(s * 0.042))
    nd.ellipse(
        [cx - ring_r, cy - ring_r, cx + ring_r, cy + ring_r],
        outline=(*NODE_RING, 180), width=max(1, int(s * 0.008))
    )

    node_layer.putalpha(
        Image.composite(node_layer.split()[3], Image.new('L', (size, size), 0), mask)
    )
    img = Image.alpha_composite(img, node_layer)

    # -- 7. Code brackets "{ }" flanking the network --
    bracket_layer = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bracket_layer)
    bw = max(2, int(s * 0.022))
    bracket_h = int(s * 0.30)
    curl = int(s * 0.055)
    b_top = cy - bracket_h // 2
    b_bot = cy + bracket_h // 2

    # Left curly brace "{"
    lx = cx - int(s * 0.35)
    # Top arm
    bd.line([(lx + curl, b_top), (lx, b_top + curl)], fill=BRACKET_CLR, width=bw)
    # Upper vertical
    bd.line([(lx, b_top + curl), (lx, cy - curl)], fill=BRACKET_CLR, width=bw)
    # Middle notch (pointing left)
    bd.line([(lx, cy - curl), (lx - curl, cy)], fill=BRACKET_CLR, width=bw)
    bd.line([(lx - curl, cy), (lx, cy + curl)], fill=BRACKET_CLR, width=bw)
    # Lower vertical
    bd.line([(lx, cy + curl), (lx, b_bot - curl)], fill=BRACKET_CLR, width=bw)
    # Bottom arm
    bd.line([(lx, b_bot - curl), (lx + curl, b_bot)], fill=BRACKET_CLR, width=bw)

    # Right curly brace "}"
    rx = cx + int(s * 0.35)
    bd.line([(rx - curl, b_top), (rx, b_top + curl)], fill=BRACKET_CLR, width=bw)
    bd.line([(rx, b_top + curl), (rx, cy - curl)], fill=BRACKET_CLR, width=bw)
    bd.line([(rx, cy - curl), (rx + curl, cy)], fill=BRACKET_CLR, width=bw)
    bd.line([(rx + curl, cy), (rx, cy + curl)], fill=BRACKET_CLR, width=bw)
    bd.line([(rx, cy + curl), (rx, b_bot - curl)], fill=BRACKET_CLR, width=bw)
    bd.line([(rx, b_bot - curl), (rx - curl, b_bot)], fill=BRACKET_CLR, width=bw)

    bracket_layer.putalpha(
        Image.composite(bracket_layer.split()[3], Image.new('L', (size, size), 0), mask)
    )
    img = Image.alpha_composite(img, bracket_layer)

    return img


# -- Platform output helpers ------------------------------------------------

def save_png(img, path):
    img.save(path, 'PNG')
    print('  [ok] %s (%dx%d)' % (path, img.size[0], img.size[1]))


def generate_icns(base_img, output_path):
    """Generate macOS .icns using iconutil."""
    with tempfile.TemporaryDirectory() as tmpdir:
        iconset_path = os.path.join(tmpdir, 'icon.iconset')
        os.makedirs(iconset_path)

        for s in [16, 32, 64, 128, 256, 512, 1024]:
            resized = base_img.resize((s, s), Image.LANCZOS)
            if s <= 512:
                resized.save(os.path.join(iconset_path, 'icon_%dx%d.png' % (s, s)))
            half = s // 2
            if half >= 16:
                resized.save(os.path.join(iconset_path, 'icon_%dx%d@2x.png' % (half, half)))

        result = subprocess.run(
            ['iconutil', '-c', 'icns', iconset_path, '-o', output_path],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print('  [FAIL] iconutil error: %s' % result.stderr)
            return False
        print('  [ok] %s (macOS .icns)' % output_path)
        return True


def generate_ico(base_img, output_path):
    """Generate Windows .ico with multiple sizes."""
    sizes = [16, 24, 32, 48, 64, 128, 256]
    imgs = [base_img.resize((s, s), Image.LANCZOS) for s in sizes]
    imgs[0].save(output_path, format='ICO',
                 sizes=[(s, s) for s in sizes],
                 append_images=imgs[1:])
    print('  [ok] %s (Windows .ico)' % output_path)


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    print('==========================================')
    print('   CodeTrellis Icon Generator')
    print('   Trellis network + code braces design')
    print('==========================================')
    print()

    master = generate_icon(1024)

    # -- macOS --
    print('macOS:')
    generate_icns(master, os.path.join(repo_root, 'resources', 'darwin', 'code.icns'))
    print()

    # -- Linux --
    print('Linux:')
    save_png(master.resize((512, 512), Image.LANCZOS),
             os.path.join(repo_root, 'resources', 'linux', 'code.png'))
    print()

    # -- Windows --
    print('Windows:')
    generate_ico(master, os.path.join(repo_root, 'resources', 'win32', 'code.ico'))
    save_png(master.resize((150, 150), Image.LANCZOS),
             os.path.join(repo_root, 'resources', 'win32', 'code_150x150.png'))
    save_png(master.resize((70, 70), Image.LANCZOS),
             os.path.join(repo_root, 'resources', 'win32', 'code_70x70.png'))
    print()

    # -- Inno Setup bitmaps --
    print('Windows Inno Setup bitmaps:')
    for scale in [100, 125, 150, 175, 200, 225, 250]:
        # Big: left panel of wizard
        bw, bh = int(164 * scale / 100), int(314 * scale / 100)
        big = Image.new('RGB', (bw, bh), BG_TOP)
        for y in range(bh):
            t = y / bh
            c = lerp_color(BG_TOP, BG_BOTTOM, t)
            ImageDraw.Draw(big).line([(0, y), (bw, y)], fill=c)
        icon_s = min(bw - 20, int(bw * 0.8))
        icon_rgba = master.resize((icon_s, icon_s), Image.LANCZOS)
        icon_rgb = Image.new('RGB', (icon_s, icon_s), BG_TOP)
        icon_rgb.paste(icon_rgba, mask=icon_rgba.split()[3])
        big.paste(icon_rgb, ((bw - icon_s) // 2, bh - icon_s - int(bh * 0.15)))
        bp = os.path.join(repo_root, 'resources', 'win32', 'inno-big-%d.bmp' % scale)
        big.save(bp, 'BMP')
        print('  [ok] %s (%dx%d)' % (bp, bw, bh))

        # Small: top-right header
        ss = int(55 * scale / 100)
        sm_rgba = master.resize((ss, ss), Image.LANCZOS)
        sm_rgb = Image.new('RGB', (ss, ss), (255, 255, 255))
        sm_rgb.paste(sm_rgba, mask=sm_rgba.split()[3])
        sp = os.path.join(repo_root, 'resources', 'win32', 'inno-small-%d.bmp' % scale)
        sm_rgb.save(sp, 'BMP')
        print('  [ok] %s (%dx%d)' % (sp, ss, ss))

    # -- Save a master PNG for reference --
    ref_path = os.path.join(repo_root, 'resources', 'codetrellis-icon-1024.png')
    master.save(ref_path, 'PNG')
    print()
    print('  [ok] %s (1024x1024 master reference)' % ref_path)

    print()
    print('All CodeTrellis icons generated!')


if __name__ == '__main__':
    main()
