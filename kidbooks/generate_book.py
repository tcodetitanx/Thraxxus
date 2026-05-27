#!/usr/bin/env python3
"""
THE ENGINEERS - Full book generation pipeline.
Uses gpt-4o-mini Responses API with reference image for consistent style.
"""

import os
import sys
import time
import base64
from openai import OpenAI
from PIL import Image
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color, white, black, HexColor

# ── Config ─────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
API_KEY = "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"
REF_IMAGE = os.path.join(SCRIPT_DIR, "family.png")
IMG_DIR = os.path.join(SCRIPT_DIR, "engineers_images")
PDF_INTERIOR = os.path.join(SCRIPT_DIR, "The_Engineers_Interior.pdf")
PDF_COVER = os.path.join(SCRIPT_DIR, "The_Engineers_Cover.pdf")

PAGE_W = 8.5 * inch
PAGE_H = 8.5 * inch
DELAY = 3  # seconds between API calls

# ── Prompt prefix (sent with every image request) ──────────────────────────
PROMPT_PREFIX = (
    "Using the attached image as a strict reference for the character faces, "
    "hair, skin tones, and the warm painterly art style, generate a new wide "
    "landscape illustration. Both toddler boys must be the EXACT same height. "
    "No character should look at the viewer -- everyone is engaged in the action. "
)

# ── Page Definitions ───────────────────────────────────────────────────────
# Each: { id, type, text (list of lines), prompt (str or None) }
# Sections are imported from build_pages.py and new_sections.py

from build_pages import ALL_SECTIONS, SECTION_ORDER, SECTION_NAMES

PAGES = [

# ── COVER ──────────────────────────────────────────────────────────────
{
    "id": "cover_front",
    "type": "cover",
    "text": [],
    "prompt": PROMPT_PREFIX + (
        "The family stands heroically on a grassy hilltop at golden hour. "
        "Mama wears stylish overalls and a tool belt, looking at the horizon. "
        "Dada wears an engineer vest and hard hat, arm around Mama looking at the view. "
        "One toddler wears a green jumpsuit with goggles and a big letter N. "
        "The other wears a blue jumpsuit with goggles and a big letter E. "
        "The golden cockapoo puppy sits at their feet. "
        "Behind them in soft focus: a steam train, a rocket, a pirate ship, "
        "a castle, a robot, a roller coaster, a space station, and a giant mech. "
        "An elephant and an owl stand nearby. Warm sunset sky, fluffy clouds. "
        "Leave clear space at the top center for a book title. Epic but inviting."
    ),
},

# ── TITLE PAGE ─────────────────────────────────────────────────────────
{
    "id": "title_page",
    "type": "title",
    "text": [],
    "prompt": PROMPT_PREFIX + (
        "The family gathers around a big wooden worktable in a warm sunlit workshop. "
        "Mama points at a blueprint. Dada holds a wrench. "
        "One boy (green overalls, letter N) and the other (blue overalls, letter E) "
        "stack colorful building blocks on the table. "
        "The golden cockapoo plays with a bolt on the floor. "
        "Pegboard wall with a few tools hanging. Sunlight through a window. "
        "Clean, warm, cozy. Leave space at top and bottom for title text. "
        "No one looks at the viewer."
    ),
},

# ── DEDICATION (text only) ────────────────────────────────────────────
{
    "id": "dedication",
    "type": "dedication",
    "text": [
        "For Neo and Ender --",
        "May you always build wonderful things together.",
        "",
        "And for Wall-E,",
        "the best helper a family could have.",
    ],
    "prompt": None,
},

# ── INTRO ──────────────────────────────────────────────────────────────
{
    "id": "intro",
    "type": "story",
    "text": [
        "In a cozy house at the end of Maple Street",
        "lived Mama, Dada, little Neo, little Ender,",
        "and their fluffy puppy Wall-E.",
        "",
        "They loved to BUILD things --",
        "big things, amazing things, impossible things!",
        "",
        "And they always helped their animal friends.",
    ],
    "prompt": PROMPT_PREFIX + (
        "A charming house with a big front yard on a sunny afternoon. "
        "Mama in a sundress tends flowers. Dada in jeans and a plaid shirt carries a toolbox. "
        "One boy (green t-shirt with letter N, khaki shorts) and the other "
        "(blue t-shirt with letter E, khaki shorts) play with building blocks "
        "and toy tools on the lawn. The puppy chases a butterfly. "
        "White picket fence, big oak tree with a tire swing, birds on the fence. "
        "Warm and inviting, simple composition."
    ),
},

# ══════════════════════════════════════════════════════════════════════
# ALL BUILD SECTIONS (28 sections x 3 pages, ordered easiest -> most amazing)
# Imported from build_pages.py
# ══════════════════════════════════════════════════════════════════════
] + [page for key in SECTION_ORDER for page in ALL_SECTIONS[key]] + [
# ── THE END ────────────────────────────────────────────────────────────
{
    "id": "the_end",
    "type": "ending",
    "text": [
        "And so Mama, Dada, Neo, Ender, and Wall-E",
        "had built the most AMAZING things",
        "with their animal friends.",
        "",
        "But their greatest adventure was always",
        "building things TOGETHER.",
        "",
        "What will YOU build today?",
        "",
        "THE END",
    ],
    "prompt": PROMPT_PREFIX + (
        "A cozy living room at sunset. The family cuddles on a big sofa. "
        "One boy in green pajamas with N and the other in blue pajamas with E "
        "are sleepy, leaning against Mama and Dada. Mama reads a book, Dada looks at the boys. "
        "The puppy is curled up asleep on a pillow. "
        "On shelves and walls behind them: dozens of small toys and models representing "
        "all their builds -- a train, rocket, airplane, pirate ship, castle, robot, "
        "monster truck, space station, mech, roller coaster, UFO, and more. "
        "Warm lamplight, cozy blanket. Through the window: orange and pink sunset. "
        "Peaceful, loving, warm."
    ),
},

# ── BACK COVER ─────────────────────────────────────────────────────────
{
    "id": "cover_back",
    "type": "back_cover",
    "text": [],
    "prompt": PROMPT_PREFIX + (
        "Simple charming scene on a cream background. "
        "The golden cockapoo puppy sits in the center surrounded by small toy versions "
        "of many builds in a loose arrangement: toy train, rocket, airplane, pirate ship, "
        "castle, robot, racecar, firetruck, tree house, roller coaster, UFO, mech suit. "
        "A couple of paw prints on the ground. An owl peeks from one side, "
        "a rabbit from the other. Clean, simple, sweet. "
        "Leave space at bottom for a text blurb and barcode area."
    ),
},
]


# ── Image Generation ───────────────────────────────────────────────────────
def load_reference():
    with open(REF_IMAGE, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def generate_image(client, ref_b64, prompt, filepath):
    """Generate one image via gpt-4o-mini Responses API with reference."""
    print(f"  Calling API...", flush=True)
    result = client.responses.create(
        model="gpt-4o-mini",
        input=[{
            "role": "user",
            "content": [
                {"type": "input_image", "image_url": f"data:image/png;base64,{ref_b64}"},
                {"type": "input_text", "text": prompt},
            ],
        }],
        tools=[{"type": "image_generation", "size": "1536x1024", "quality": "high"}],
    )

    for item in result.output:
        if item.type == "image_generation_call":
            img_bytes = base64.b64decode(item.result)
            with open(filepath, "wb") as f:
                f.write(img_bytes)
            print(f"  Saved: {os.path.basename(filepath)} ({len(img_bytes)//1024}KB)", flush=True)
            return True

    print(f"  WARNING: No image in response", flush=True)
    return False


def generate_all_images():
    os.makedirs(IMG_DIR, exist_ok=True)
    client = OpenAI(api_key=API_KEY)
    ref_b64 = load_reference()

    pages_with_images = [p for p in PAGES if p.get("prompt")]
    total = len(pages_with_images)
    failed = []

    for i, page in enumerate(pages_with_images):
        filepath = os.path.join(IMG_DIR, f"{page['id']}.png")

        # Skip existing valid images
        if os.path.exists(filepath):
            try:
                img = Image.open(filepath)
                img.verify()
                print(f"[{i+1}/{total}] SKIP (exists): {page['id']}", flush=True)
                continue
            except Exception:
                pass

        print(f"[{i+1}/{total}] {page['id']}...", flush=True)
        try:
            success = generate_image(client, ref_b64, page["prompt"], filepath)
            if not success:
                failed.append(page["id"])
        except Exception as e:
            print(f"  ERROR: {e}", flush=True)
            # Retry once
            print(f"  Retrying in 10s...", flush=True)
            time.sleep(10)
            try:
                success = generate_image(client, ref_b64, page["prompt"], filepath)
                if not success:
                    failed.append(page["id"])
            except Exception as e2:
                print(f"  RETRY FAILED: {e2}", flush=True)
                failed.append(page["id"])

        if i < total - 1:
            time.sleep(DELAY)

    print(f"\n{'='*50}", flush=True)
    print(f"Done: {total - len(failed)}/{total} images", flush=True)
    if failed:
        print(f"Failed: {failed}", flush=True)
    return len(failed) == 0


# ── PDF Helpers ────────────────────────────────────────────────────────────
def compress_image(img_path, max_w=1536, max_h=1024, quality=62):
    """Compress image to JPEG for PDF embedding."""
    img = Image.open(img_path)
    if img.mode == "RGBA":
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")
    img.thumbnail((max_w, max_h), Image.LANCZOS)
    out = img_path.replace(".png", "_c.jpg")
    img.save(out, "JPEG", quality=quality, optimize=True)
    return out


def crop_to_square(img_path, quality=90):
    """Crop a wide image to square (center crop) and save as JPEG."""
    img = Image.open(img_path)
    if img.mode == "RGBA":
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")
    w, h = img.size
    # Center crop to square based on the shorter dimension
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    img = img.crop((left, top, left + side, top + side))
    out = img_path.replace(".png", "_sq.jpg")
    img.save(out, "JPEG", quality=quality, optimize=True)
    return out


# ── Typography Setup ───────────────────────────────────────────────────────
import re

# Sound effect patterns: all-caps words, onomatopoeia
SFX_PATTERN = re.compile(
    r'^(CHOO|ZOOM|BLAST|BEEP|WHIRR|WHOOO|SCOOP|CRASH|SQUAWK|CHOMP|5\.\.\.|THE END'
    r'|FWOO|SPLAT|VROOM|HONK|BRAAA|WEEEE|RRRUMM|CRUSH|CRUNCH|ROAAA|VROO|CLICK'
    r'|ARRR|STOMP|BZZZ)',
)

def _is_sfx(line):
    """Is this line a sound effect or big exclamation?"""
    return bool(SFX_PATTERN.match(line.strip()))

def _is_dialogue(line):
    """Is this line spoken dialogue?"""
    s = line.strip()
    return s.startswith('"') or s.startswith("'") or s.startswith('\u201c')

def _register_fonts():
    """Register nice Windows system fonts."""
    from reportlab.pdfbase import pdfmetrics as pm
    from reportlab.pdfbase.ttfonts import TTFont as TF
    font_dir = r"C:\Windows\Fonts"
    try:
        # Body fonts
        pm.registerFont(TF("Body", os.path.join(font_dir, "verdana.ttf")))
        pm.registerFont(TF("Body-Bold", os.path.join(font_dir, "verdanab.ttf")))
        pm.registerFont(TF("Body-Italic", os.path.join(font_dir, "verdanai.ttf")))
        pm.registerFont(TF("Body-BoldItalic", os.path.join(font_dir, "verdanaz.ttf")))
        # Dialogue fonts (Georgia - warm serif)
        pm.registerFont(TF("Dialogue", os.path.join(font_dir, "georgia.ttf")))
        pm.registerFont(TF("Dialogue-Bold", os.path.join(font_dir, "georgiab.ttf")))
        pm.registerFont(TF("Dialogue-Italic", os.path.join(font_dir, "georgiai.ttf")))
        pm.registerFont(TF("Dialogue-BoldItalic", os.path.join(font_dir, "georgiaz.ttf")))
        # Impact for sound effects
        pm.registerFont(TF("SFX", os.path.join(font_dir, "impact.ttf")))
        # Trebuchet for titles
        pm.registerFont(TF("Title", os.path.join(font_dir, "trebucbd.ttf")))
        pm.registerFont(TF("Title-Regular", os.path.join(font_dir, "trebuc.ttf")))
        print("  Registered system fonts (Verdana, Georgia, Impact, Trebuchet)", flush=True)
        return True
    except Exception as e:
        print(f"  Font registration failed: {e}, using defaults", flush=True)
        return False

# Color palette
CLR_NARRATION = HexColor("#3B2F1E")    # warm dark brown
CLR_DIALOGUE = HexColor("#1A3A5C")     # deep navy blue
CLR_SFX = HexColor("#C13B2A")          # bold red
CLR_PANEL_BG = HexColor("#FDF6E3")     # warm cream
CLR_PANEL_BORDER = HexColor("#D4B896") # warm tan
CLR_PAGE_BG = HexColor("#FFFDF5")      # off-white


def draw_story_text(c, lines, panel_x, panel_y, panel_w, panel_h, has_fonts):
    """Draw left-justified story text with proper padding inside panel."""
    PAD_LEFT = 0.4 * inch
    PAD_RIGHT = 0.4 * inch
    PAD_TOP = 0.3 * inch
    PAD_BOTTOM = 0.25 * inch

    text_x = panel_x + PAD_LEFT
    text_w = panel_w - PAD_LEFT - PAD_RIGHT

    # Classify lines
    styled = []
    for line in lines:
        s = line.strip()
        if s == "":
            styled.append(("gap", "", 0))
        elif s == "THE END":
            styled.append(("theend", s, 0))
        elif _is_sfx(s):
            styled.append(("sfx", s, 0))
        elif _is_dialogue(s):
            styled.append(("dialogue", s, 0))
        else:
            styled.append(("narration", s, 0))

    # Calculate total text height for vertical centering
    total_h = 0
    for kind, text, _ in styled:
        if kind == "gap":
            total_h += 14
        elif kind == "theend":
            total_h += 44
        elif kind == "sfx":
            total_h += 30
        else:
            total_h += 23

    available_h = panel_h - PAD_TOP - PAD_BOTTOM
    start_y = panel_y + panel_h - PAD_TOP - max(0, (available_h - total_h) / 2)
    y = start_y

    for kind, text, _ in styled:
        if kind == "gap":
            y -= 14
            continue

        if kind == "theend":
            font = "SFX" if has_fonts else "Helvetica-Bold"
            c.setFillColor(HexColor("#8B6914"))
            c.setFont(font, 30)
            c.drawString(text_x, y - 6, text)
            y -= 44
        elif kind == "sfx":
            font = "SFX" if has_fonts else "Helvetica-Bold"
            c.setFillColor(CLR_SFX)
            c.setFont(font, 21)
            c.drawString(text_x, y, text)
            y -= 30
        elif kind == "dialogue":
            font = "Dialogue-Italic" if has_fonts else "Helvetica-BoldOblique"
            c.setFillColor(CLR_DIALOGUE)
            c.setFont(font, 15)
            c.drawString(text_x, y, text)
            y -= 23
        else:
            font = "Body" if has_fonts else "Helvetica"
            c.setFillColor(CLR_NARRATION)
            c.setFont(font, 14.5)
            c.drawString(text_x, y, text)
            y -= 23


def draw_decorative_divider(c, cx, y, width=1.5*inch):
    """Draw a small decorative divider (dots and line)."""
    c.setStrokeColor(HexColor("#D4B896"))
    c.setFillColor(HexColor("#D4B896"))
    c.setLineWidth(0.75)
    # Center line with dots
    c.line(cx - width/2, y, cx - 6, y)
    c.circle(cx, y, 2.5, fill=1, stroke=0)
    c.line(cx + 6, y, cx + width/2, y)


# ── PDF Creation ───────────────────────────────────────────────────────────
def create_interior_pdf():
    print("\nCreating interior PDF...", flush=True)
    c = canvas.Canvas(PDF_INTERIOR, pagesize=(PAGE_W, PAGE_H))
    has_fonts = _register_fonts()

    page_num = 0
    for page in PAGES:
        if page["type"] in ("cover", "back_cover"):
            continue

        page_num += 1

        # ── DEDICATION ──
        if page["type"] == "dedication":
            c.setFillColor(HexColor("#FFF8DC"))
            c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

            # Decorative top divider
            draw_decorative_divider(c, PAGE_W / 2, PAGE_H / 2 + 1.2 * inch, 2 * inch)

            # Dedication text in warm italic serif
            font_ded = "Dialogue-Italic" if has_fonts else "Helvetica-Oblique"
            c.setFillColor(HexColor("#5B4A1E"))
            y = PAGE_H / 2 + 0.7 * inch
            for line in page["text"]:
                if line == "":
                    y -= 18
                    continue
                c.setFont(font_ded, 19)
                tw = c.stringWidth(line, font_ded, 19)
                c.drawString((PAGE_W - tw) / 2, y, line)
                y -= 30

            # Decorative bottom divider
            draw_decorative_divider(c, PAGE_W / 2, y - 0.2 * inch, 2 * inch)

            c.showPage()
            continue

        # ── TITLE PAGE ──
        if page["type"] == "title":
            c.setFillColor(HexColor("#FFF8DC"))
            c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

            img_path = os.path.join(IMG_DIR, f"{page['id']}.png")
            if os.path.exists(img_path):
                jpg = compress_image(img_path)
                iw = 7.0 * inch
                ih = iw * (1024 / 1536)
                ix = (PAGE_W - iw) / 2
                iy = 0.9 * inch

                c.drawImage(jpg, ix, iy, iw, ih, preserveAspectRatio=True)

            # Title
            title_font = "Title" if has_fonts else "Helvetica-Bold"
            c.setFillColor(HexColor("#6B4F1D"))
            c.setFont(title_font, 50)
            t = "THE ENGINEERS"
            tw = c.stringWidth(t, title_font, 50)
            c.drawString((PAGE_W - tw) / 2, 7.0 * inch, t)

            # Decorative line under title
            draw_decorative_divider(c, PAGE_W / 2, 6.85 * inch, 3 * inch)

            # Subtitle
            sub_font = "Title-Regular" if has_fonts else "Helvetica"
            c.setFillColor(HexColor("#8B6914"))
            c.setFont(sub_font, 17)
            s = "A Building Adventure"
            sw = c.stringWidth(s, sub_font, 17)
            c.drawString((PAGE_W - sw) / 2, 6.55 * inch, s)

            c.showPage()
            continue

        # ── STORY / ENDING PAGES ──
        # Layout: text panel at bottom, image fills everything above it
        c.setFillColor(CLR_PAGE_BG)
        c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

        # First, draw the text panel at the bottom so we know where the image ends
        panel_margin = 0.3 * inch
        panel_x = panel_margin
        panel_w = PAGE_W - 2 * panel_margin
        panel_bottom = 0.3 * inch
        panel_h = 2.75 * inch  # fixed height for text area
        panel_y = panel_bottom

        if page["text"]:
            # Panel background
            c.setFillColor(CLR_PANEL_BG)
            c.setStrokeColor(CLR_PANEL_BORDER)
            c.setLineWidth(1.2)
            c.roundRect(panel_x, panel_y, panel_w, panel_h,
                       radius=14, fill=1, stroke=1)

            # Draw the styled text
            draw_story_text(c, page["text"],
                          panel_x, panel_y,
                          panel_w, panel_h,
                          has_fonts)

        # Image sits above the text panel — drawn clean, no overlays
        img_path = os.path.join(IMG_DIR, f"{page['id']}.png")
        if os.path.exists(img_path):
            jpg = compress_image(img_path)
            img_margin = 0.25 * inch
            img_top = PAGE_H - img_margin
            img_gap = 0.15 * inch
            panel_top_edge = panel_y + panel_h + img_gap

            iw = PAGE_W - 2 * img_margin
            ih = img_top - panel_top_edge
            ix = img_margin
            iy = panel_top_edge

            c.drawImage(jpg, ix, iy, iw, ih, preserveAspectRatio=True)

        # Page number (small, subtle, bottom center)
        if page["type"] == "story" and page_num > 3:
            pn_font = "Body" if has_fonts else "Helvetica"
            c.setFillColor(HexColor("#B8A88A"))
            c.setFont(pn_font, 9)
            pn_text = str(page_num - 2)
            tw = c.stringWidth(pn_text, pn_font, 9)
            c.drawString((PAGE_W - tw) / 2, 0.13 * inch, pn_text)

        c.showPage()

    c.save()
    size_mb = os.path.getsize(PDF_INTERIOR) / (1024 * 1024)
    print(f"Interior PDF: {PDF_INTERIOR} ({size_mb:.1f} MB)", flush=True)
    return size_mb


def create_cover_pdf():
    print("\nCreating cover PDF...", flush=True)
    COVER_W = 8.75 * inch
    COVER_H = 8.75 * inch
    c = canvas.Canvas(PDF_COVER, pagesize=(COVER_W, COVER_H))

    # ── FRONT COVER ──
    img_path = os.path.join(IMG_DIR, "cover_front.png")
    if os.path.exists(img_path):
        jpg = crop_to_square(img_path, 92)
        c.drawImage(jpg, 0, 0, COVER_W, COVER_H, preserveAspectRatio=True)

    # Title band
    band_h = 1.6 * inch
    band_y = COVER_H - band_h - 0.4 * inch
    c.setFillColor(Color(0, 0, 0, alpha=0.4))
    c.rect(0, band_y, COVER_W, band_h, fill=1, stroke=0)

    c.setFillColor(HexColor("#FFD700"))
    c.setFont("Helvetica-Bold", 60)
    t = "THE ENGINEERS"
    tw = c.stringWidth(t, "Helvetica-Bold", 60)
    c.drawString((COVER_W - tw) / 2, band_y + band_h - 0.7 * inch, t)

    c.setFillColor(white)
    c.setFont("Helvetica", 20)
    s = "A Building Adventure with Animal Friends"
    sw = c.stringWidth(s, "Helvetica", 20)
    c.drawString((COVER_W - sw) / 2, band_y + 0.3 * inch, s)

    c.showPage()

    # ── BACK COVER ──
    c.setFillColor(HexColor("#FFF8DC"))
    c.rect(0, 0, COVER_W, COVER_H, fill=1, stroke=0)

    img_path = os.path.join(IMG_DIR, "cover_back.png")
    if os.path.exists(img_path):
        jpg = compress_image(img_path, 1600, 1100, 85)
        iw = 6.5 * inch
        ih = iw * (1024 / 1536)
        ix = (COVER_W - iw) / 2
        iy = (COVER_H - ih) / 2 + 0.8 * inch
        c.drawImage(jpg, ix, iy, iw, ih, preserveAspectRatio=True)

    c.setFillColor(HexColor("#4B0082"))
    c.setFont("Helvetica", 13)
    blurb = [
        "Join Mama, Dada, Neo, Ender, and their puppy Wall-E",
        "as they help animals in trouble and team up",
        "to build incredible things together!",
        "",
        "From tree houses to space stations,",
        "there's nothing this family can't build!",
    ]
    y = 2.2 * inch
    for line in blurb:
        if line == "":
            y -= 8
            continue
        tw = c.stringWidth(line, "Helvetica", 13)
        c.drawString((COVER_W - tw) / 2, y, line)
        y -= 18

    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(HexColor("#8B6914"))
    age = "Ages 2-5"
    tw = c.stringWidth(age, "Helvetica-Bold", 12)
    c.drawString((COVER_W - tw) / 2, 0.8 * inch, age)

    c.showPage()
    c.save()
    size_mb = os.path.getsize(PDF_COVER) / (1024 * 1024)
    print(f"Cover PDF: {PDF_COVER} ({size_mb:.1f} MB)", flush=True)
    return size_mb


def create_final_pdf():
    """Create a single combined PDF: front cover + interior + back cover."""
    from PyPDF2 import PdfMerger, PdfReader
    FINAL_PATH = os.path.join(SCRIPT_DIR, "The_Engineers_FINAL.pdf")
    print("\nCreating combined final PDF...", flush=True)

    # We need to create separate temp PDFs for front cover and back cover
    # at the interior page size (8.5x8.5) so they merge cleanly
    FRONT_TEMP = os.path.join(SCRIPT_DIR, "_temp_front.pdf")
    BACK_TEMP = os.path.join(SCRIPT_DIR, "_temp_back.pdf")

    # ── Front cover at 8.5x8.5 ──
    c = canvas.Canvas(FRONT_TEMP, pagesize=(PAGE_W, PAGE_H))
    img_path = os.path.join(IMG_DIR, "cover_front.png")
    if os.path.exists(img_path):
        jpg = crop_to_square(img_path, 92)
        c.drawImage(jpg, 0, 0, PAGE_W, PAGE_H, preserveAspectRatio=True)

    # Title band
    band_h = 1.5 * inch
    band_y = PAGE_H - band_h - 0.35 * inch
    c.setFillColor(Color(0, 0, 0, alpha=0.4))
    c.rect(0, band_y, PAGE_W, band_h, fill=1, stroke=0)

    c.setFillColor(HexColor("#FFD700"))
    c.setFont("Helvetica-Bold", 56)
    t = "THE ENGINEERS"
    tw = c.stringWidth(t, "Helvetica-Bold", 56)
    c.drawString((PAGE_W - tw) / 2, band_y + band_h - 0.65 * inch, t)

    c.setFillColor(white)
    c.setFont("Helvetica", 18)
    s = "A Building Adventure with Animal Friends"
    sw = c.stringWidth(s, "Helvetica", 18)
    c.drawString((PAGE_W - sw) / 2, band_y + 0.3 * inch, s)
    c.showPage()
    c.save()

    # ── Back cover at 8.5x8.5 ──
    c = canvas.Canvas(BACK_TEMP, pagesize=(PAGE_W, PAGE_H))
    c.setFillColor(HexColor("#FFF8DC"))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    img_path = os.path.join(IMG_DIR, "cover_back.png")
    if os.path.exists(img_path):
        jpg = compress_image(img_path, 1600, 1100, 85)
        iw = 6.0 * inch
        ih = iw * (1024 / 1536)
        ix = (PAGE_W - iw) / 2
        iy = (PAGE_H - ih) / 2 + 0.8 * inch
        c.drawImage(jpg, ix, iy, iw, ih, preserveAspectRatio=True)

    c.setFillColor(HexColor("#4B0082"))
    c.setFont("Helvetica", 13)
    blurb = [
        "Join Mama, Dada, Neo, Ender, and their puppy Wall-E",
        "as they help animals in trouble and team up",
        "to build incredible things together!",
        "",
        "From tree houses to space stations,",
        "there's nothing this family can't build!",
    ]
    y = 2.2 * inch
    for line in blurb:
        if line == "":
            y -= 8
            continue
        tw = c.stringWidth(line, "Helvetica", 13)
        c.drawString((PAGE_W - tw) / 2, y, line)
        y -= 18

    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(HexColor("#8B6914"))
    age = "Ages 2-5"
    tw = c.stringWidth(age, "Helvetica-Bold", 12)
    c.drawString((PAGE_W - tw) / 2, 0.8 * inch, age)
    c.showPage()
    c.save()

    # ── Merge: front cover + interior + back cover ──
    merger = PdfMerger()
    merger.append(FRONT_TEMP)
    merger.append(PDF_INTERIOR)
    merger.append(BACK_TEMP)
    merger.write(FINAL_PATH)
    merger.close()

    # Clean up temp files
    os.remove(FRONT_TEMP)
    os.remove(BACK_TEMP)

    size_mb = os.path.getsize(FINAL_PATH) / (1024 * 1024)
    print(f"Final PDF: {FINAL_PATH} ({size_mb:.1f} MB)", flush=True)
    return size_mb


# ── Main ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50, flush=True)
    print("  THE ENGINEERS - Book Generator", flush=True)
    print("=" * 50, flush=True)

    step = sys.argv[1] if len(sys.argv) > 1 else "all"

    if step in ("all", "images"):
        print(f"\n[STEP 1] Generating {sum(1 for p in PAGES if p.get('prompt'))} images...", flush=True)
        generate_all_images()

    if step in ("all", "pdf"):
        print("\n[STEP 2] Creating PDFs...", flush=True)
        interior_mb = create_interior_pdf()
        cover_mb = create_cover_pdf()
        final_mb = create_final_pdf()

        if final_mb > 30:
            print("WARNING: Over 30MB! May need recompression.", flush=True)

    print("\n" + "=" * 50, flush=True)
    print("  COMPLETE!", flush=True)
    print(f"  Final:    {os.path.join(SCRIPT_DIR, 'The_Engineers_FINAL.pdf')}", flush=True)
    print(f"  Interior: {PDF_INTERIOR}", flush=True)
    print(f"  Cover:    {PDF_COVER}", flush=True)
    print("=" * 50, flush=True)
