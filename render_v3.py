#!/usr/bin/env python3
"""Render the v3 broadsheet: THE WORLD TODAY - Thursday, 19 November 2026.

Draws the whole 1024x1024 front page with PIL + local DejaVu fonts.
All news text was researched from real reporting on 19 Nov 2026.
Output: entry.png (1024x1024, <= 1 MiB).
"""
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
CREAM = (246, 239, 219)
PAPER = (250, 244, 228)
NAVY = (21, 38, 71)
NAVY2 = (38, 58, 96)
GOLD = (168, 135, 46)
GOLD_LT = (196, 164, 74)
INK = (30, 30, 28)
RULE = (21, 38, 71)
SKY = (214, 226, 232)

FD = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FD + name, size)


SERIF = "DejaVuSerif.ttf"
SERIF_B = "DejaVuSerif-Bold.ttf"
SANS = "DejaVuSans.ttf"
SANS_B = "DejaVuSans-Bold.ttf"


def wrap(draw, text, fnt, max_w):
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.28)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def draw_center(draw, text, y, fnt, fill, cx=W // 2):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + int(fnt.size * 1.3)


def hrule(draw, x0, x1, y, width=2, fill=RULE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def frame(draw, box, fill=NAVY, width=2):
    draw.rectangle(box, outline=fill, width=width)


# ---------------------------------------------------------------- illustrations
def art_lead():
    """Summit hall: three flags above a long table, three seated figures."""
    img = Image.new("RGB", (428, 176), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 427, 175], fill=(232, 222, 196))
    for x in (18, 158, 298):
        d.rectangle([x, 10, x + 110, 84], fill=SKY, outline=NAVY, width=2)
        d.arc([x, 10, x + 110, 64], 180, 360, fill=NAVY, width=2)
        d.line([(x + 55, 10), (x + 55, 84)], fill=NAVY, width=2)
        d.line([(x, 48), (x + 110, 48)], fill=NAVY, width=1)

    def flag_us(x, y):
        d.rectangle([x, y, x + 52, y + 30], fill=(178, 34, 52), outline=NAVY, width=1)
        for i in range(3):
            d.rectangle([x, y + 5 + i * 9, x + 52, y + 8 + i * 9], fill=(246, 239, 219))
        d.rectangle([x, y, x + 22, y + 15], fill=NAVY)
        for sx in (4, 12, 20):
            for sy in (4, 10):
                d.ellipse([x + sx - 1, y + sy - 1, x + sx + 1, y + sy + 1], fill=(246, 239, 219))

    def flag_cn(x, y):
        d.rectangle([x, y, x + 52, y + 30], fill=(190, 30, 30), outline=NAVY, width=1)
        d.regular_polygon((x + 13, y + 10, 5), 5, fill=(246, 220, 90))
        for sx, sy in ((30, 5), (36, 10), (36, 16), (30, 20)):
            d.regular_polygon((x + sx, y + sy, 3), 5, fill=(246, 220, 90))

    def flag_ru(x, y):
        d.rectangle([x, y, x + 52, y + 30], fill=(246, 239, 219), outline=NAVY, width=1)
        d.rectangle([x, y + 10, x + 52, y + 20], fill=(28, 68, 160))
        d.rectangle([x, y + 20, x + 52, y + 30], fill=(190, 30, 30))

    flag_us(48, 92)
    flag_cn(188, 92)
    flag_ru(328, 92)
    for x in (48, 188, 328):
        d.line([(x + 26, 92), (x + 26, 132)], fill=NAVY, width=2)
    d.rectangle([20, 132, 408, 141], fill=NAVY)
    d.rectangle([30, 141, 60, 168], fill=NAVY2)
    d.rectangle([368, 141, 398, 168], fill=NAVY2)
    for cx in (110, 214, 318):
        d.ellipse([cx - 12, 116, cx + 12, 140], fill=NAVY)
        d.polygon([(cx - 24, 168), (cx - 18, 140), (cx + 18, 140), (cx + 24, 168)],
                  fill=NAVY)
    d.rectangle([0, 168, 427, 175], fill=(200, 186, 150))
    frame(d, [0, 0, 427, 175])
    return img


def art_icj():
    """The Hague court: columned facade with scales of justice."""
    img = Image.new("RGB", (305, 125), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 304, 124], fill=(232, 222, 196))
    d.polygon([(40, 34), (152, 8), (264, 34)], fill=NAVY)
    d.polygon([(52, 30), (152, 12), (252, 30)], fill=GOLD_LT)
    for x in (58, 108, 158, 208):
        d.rectangle([x, 34, x + 16, 108], fill=(246, 239, 219), outline=NAVY, width=2)
        d.rectangle([x - 3, 30, x + 19, 36], fill=NAVY)
        d.rectangle([x - 3, 106, x + 19, 112], fill=NAVY)
    d.rectangle([40, 108, 264, 116], fill=NAVY)
    d.line([(152, 16), (152, 28)], fill=NAVY, width=2)
    d.line([(138, 20), (166, 20)], fill=NAVY, width=2)
    d.polygon([(136, 20), (140, 28), (132, 28)], fill=NAVY)
    d.polygon([(164, 20), (168, 28), (160, 28)], fill=NAVY)
    frame(d, [0, 0, 304, 124])
    return img


def art_gta():
    """Vice City dusk: skyline, sun, palm silhouettes."""
    img = Image.new("RGB", (305, 125), PAPER)
    d = ImageDraw.Draw(img)
    for i, col in enumerate(((250, 196, 120), (240, 150, 80), (220, 110, 70),
                             (190, 80, 70), (150, 70, 90))):
        d.rectangle([0, i * 16, 304, (i + 1) * 16], fill=col)
    d.ellipse([118, 18, 186, 86], fill=(252, 230, 150), outline=(200, 120, 40), width=2)
    for x, w, h in ((0, 34, 52), (36, 26, 70), (64, 40, 44), (106, 30, 62),
                    (138, 44, 38), (184, 30, 66), (216, 38, 48), (256, 48, 74)):
        d.rectangle([x, 110 - h, x + w, 110], fill=NAVY)
        for wy in range(110 - h + 6, 106, 12):
            for wx in range(x + 5, x + w - 4, 10):
                d.rectangle([wx, wy, wx + 4, wy + 5], fill=(250, 220, 130))

    def palm(x, y, s=1.0):
        d.line([(x, y), (x + 4 * s, y - 34 * s)], fill=NAVY, width=3)
        for dx, dy in ((-16, -34), (-8, -40), (6, -42), (16, -36), (20, -28), (-20, -26)):
            d.line([(x + 4 * s, y - 34 * s),
                    (x + 4 * s + dx * s, y - 34 * s + dy * s * 0.4)], fill=NAVY, width=2)
    palm(18, 124, 0.9)
    palm(288, 124, 0.8)
    d.rectangle([0, 110, 304, 124], fill=(60, 40, 60))
    frame(d, [0, 0, 304, 124])
    return img


def art_bridge():
    """Crimean Bridge at night: span over water, smoke, searchlights."""
    img = Image.new("RGB", (305, 125), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 304, 124], fill=(24, 34, 58))
    for sx, sy in ((20, 12), (70, 20), (130, 8), (200, 16), (260, 10), (290, 26),
                   (100, 30), (230, 30)):
        d.ellipse([sx, sy, sx + 2, sy + 2], fill=(246, 239, 219))
    for x0, x1 in ((40, 150), (260, 170)):
        d.polygon([(x0, 110), (x1, 10), (x1 + 14, 10), (x0 + 8, 110)], fill=(240, 230, 180))
    for cx, cy, r in ((120, 40, 16), (140, 28, 20), (160, 38, 14), (175, 26, 12)):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(150, 150, 150))
        d.ellipse([cx - r + 4, cy - r + 5, cx + r - 4, cy + r - 5], fill=(180, 180, 180))
    d.rectangle([0, 78, 304, 88], fill=(200, 200, 200))
    d.arc([60, 30, 244, 110], 180, 360, fill=(220, 220, 220), width=4)
    for x in (80, 120, 160, 200):
        d.line([(x, 78), (x, 62)], fill=(220, 220, 220), width=3)
    d.rectangle([138, 76, 168, 90], fill=(24, 34, 58))
    d.polygon([(138, 78), (152, 66), (168, 78)], fill=(24, 34, 58))
    for yy in range(92, 124, 6):
        d.line([(0, yy), (304, yy)], fill=(90, 120, 150), width=1)
    frame(d, [0, 0, 304, 124])
    return img


def art_vangogh():
    """Blossoming chestnut tree with blossom clusters, church spire behind."""
    img = Image.new("RGB", (305, 125), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 304, 124], fill=(214, 226, 210))
    d.rectangle([228, 52, 262, 124], fill=(120, 90, 70))
    d.polygon([(224, 52), (245, 14), (266, 52)], fill=NAVY)
    d.rectangle([238, 66, 252, 84], fill=(246, 239, 219))
    d.polygon([(88, 124), (100, 64), (116, 64), (128, 124)], fill=(90, 60, 40))
    for x0, y0, x1, y1 in ((100, 72, 46, 38), (106, 66, 152, 28), (104, 78, 178, 56),
                           (110, 62, 76, 32)):
        d.line([(x0, y0), (x1, y1)], fill=(90, 60, 40), width=4)
    rnd = random.Random(1911)
    for _ in range(420):
        cx = rnd.randint(28, 200)
        cy = rnd.randint(10, 68)
        r = rnd.randint(2, 6)
        col = rnd.choice([(250, 248, 240), (244, 214, 222), (236, 200, 210),
                          (220, 235, 220), (250, 240, 200)])
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col, outline=(120, 140, 110), width=1)
    d.rectangle([0, 114, 304, 124], fill=(110, 140, 90))
    frame(d, [0, 0, 304, 124])
    return img


# ---------------------------------------------------------------- front page
def build():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    MX = 36
    RX = W - MX

    # ---- masthead
    y = draw_center(d, "THE WORLD TODAY", 14, font(SERIF_B, 76), NAVY)
    hrule(d, MX, RX, 106, 3)
    hrule(d, MX, RX, 111, 1)
    draw_center(d, "THURSDAY, 19 NOVEMBER 2026", 122, font(SERIF_B, 28), NAVY)
    draw_center(d, "ONE IMAGE  ·  THE WHOLE DAY  ·  SHENZHEN — THE HAGUE — NEW YORK",
                158, font(SANS, 14), NAVY2)
    hrule(d, MX, RX, 184, 2)

    # ---- LEAD: kicker + headline + deck full width
    y = 194
    d.text((MX, y), "THE LEAD — SHENZHEN, CHINA", font=font(SANS_B, 18), fill=GOLD)
    y += 28
    d.text((MX, y), "THREE AT ONE TABLE", font=font(SERIF_B, 48), fill=NAVY)
    y += 60
    y = draw_lines(d, wrap(d,
        "Trump, Xi and Putin sign a four-point peace declaration after "
        "90 minutes — nuclear arms, energy and the UN on the table.",
        font(SERIF, 21), RX - MX), MX, y, font(SERIF, 21), NAVY2, leading=27)
    hrule(d, MX, RX, y + 8, 1)

    # ---- lead body (left) + art (right)
    y += 18
    body_top = y
    draw_lines(d, wrap(d,
        "Xi Jinping hosts Donald Trump and Vladimir Putin at APEC in "
        "Shenzhen — the first trilateral meeting of the three leaders. "
        "Their “Heads of State Declaration toward Peace” vows a nuclear "
        "war “cannot be won and must never be fought”, backs UN reform "
        "and steadier energy supplies. It says nothing of Ukraine or "
        "Iran. Trump flies home tonight.",
        font(SERIF, 18), 500), MX, body_top, font(SERIF, 18), INK, leading=24)
    img.paste(art_lead(), (560, body_top))
    d.text((560, body_top + 180),
           "The three leaders meet on the sidelines of APEC.",
           font=font(SERIF, 13), fill=NAVY2)
    lead_end = body_top + 198
    hrule(d, MX, RX, lead_end, 2)

    # ---- four-column row
    cols = [
        ("THE HAGUE", "GENOCIDE, THE COURT RULES",
         "The world court finds Myanmar committed genocide against the "
         "Rohingya in 2017 — the first state ever held responsible. "
         "Nine to six; reparations ordered.", art_icj()),
        ("LOS ANGELES", "VICE CITY'S $2.36BN DAY",
         "GTA VI launches after 13 years. An estimated 24.6m copies "
         "sold on day one, about $2.36bn — the biggest entertainment "
         "launch on record.", art_gta()),
        ("KERCH STRAIT", "THE BRIDGE HIT AGAIN",
         "Third strike this week: the rail span is hit overnight and "
         "traffic halts. Kyiv presses its campaign on Russia's fuel "
         "lines.", art_bridge()),
        ("NEW YORK", "A RECORD $190.4M",
         "Van Gogh's Blossoming Chestnut Trees sets an artist record "
         "at Sotheby's, after a Nazi-era ownership dispute is settled.",
         art_vangogh()),
    ]
    cw, gap = 226, 12
    y0 = lead_end + 14
    art_w, art_h = 226, 82
    col_bottom = y0
    for i, (kick, head, body, art) in enumerate(cols):
        x = MX + i * (cw + gap)
        img.paste(art.resize((art_w, art_h), Image.LANCZOS), (x, y0))
        yy = y0 + art_h + 8
        d.text((x, yy), kick, font=font(SANS_B, 11), fill=GOLD)
        yy += 17
        yy = draw_lines(d, wrap(d, head, font(SERIF_B, 22), cw),
                        x, yy, font(SERIF_B, 22), NAVY, leading=25)
        yy += 3
        yy = draw_lines(d, wrap(d, body, font(SERIF, 15), cw),
                        x, yy, font(SERIF, 15), INK, leading=19)
        col_bottom = max(col_bottom, yy)
    row_end = col_bottom + 8
    hrule(d, MX, RX, row_end, 2)

    # ---- ALSO TODAY strip
    y = row_end + 10
    d.text((MX, y), "ALSO TODAY", font=font(SANS_B, 16), fill=GOLD)
    items = [
        ("NVIDIA", "Record $115.8bn revenue; shares fall 2.9%."),
        ("THE SENATE", "Rejects the Iran war-powers resolution, 51–48."),
        ("HORMUZ", "ADNOC tanker hit; 11 hurt, one missing."),
        ("UKRAINE AID", "EU proposes a €45bn loan for Kyiv."),
        ("CYCLONE AKVAN", "Odisha evacuates 46,701; landfall Friday."),
        ("VOYAGER 1", "One light-day from Earth — 25.9bn km, a first."),
    ]
    col_w = (RX - MX) // 2
    f_label = font(SANS_B, 14)
    f_text = font(SERIF, 14)
    for i, (lab, txt) in enumerate(items):
        cx = MX + (i % 2) * col_w
        cy = y + 28 + (i // 2) * 30
        d.text((cx, cy), lab, font=f_label, fill=NAVY)
        lw = d.textlength(lab, font=f_label)
        tx = cx + lw + 10
        lines = wrap(d, "—  " + txt, f_text, RX - tx if i % 2 else cx + col_w - tx - 8)
        draw_lines(d, lines, tx, cy, f_text, INK, leading=18)
    strip_end = y + 28 + 3 * 30
    print("layout: lead_end", lead_end, "row_end", row_end,
          "strip_end", strip_end, "footer_y", strip_end + 10)
    hrule(d, MX, RX, strip_end + 4, 1)
    draw_center(d, "THE WORLD TODAY  ·  THURSDAY, 19 NOVEMBER 2026  ·  "
                   "ALL STORIES REPORTED TODAY",
                strip_end + 10, font(SANS, 11), NAVY2)
    return img


if __name__ == "__main__":
    page = build()
    page.save("entry.png", optimize=True)
    import os
    print("saved entry.png", os.path.getsize("entry.png"), "bytes")
