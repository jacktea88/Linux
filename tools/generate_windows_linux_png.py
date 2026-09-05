from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = []
    if bold:
        candidates.extend([
            "C:/Windows/Fonts/msjhbd.ttc",
            "C:/Windows/Fonts/NotoSansTC-Bold.otf",
        ])
    candidates.extend([
        "C:/Windows/Fonts/msjh.ttc",
        "C:/Windows/Fonts/NotoSansTC-Regular.otf",
        "C:/Windows/Fonts/arial.ttf",
    ])

    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def center_text(draw: ImageDraw.ImageDraw, box, text, font, fill=(17, 24, 39)):
    x1, y1, x2, y2 = box
    bbox = draw.multiline_textbbox((0, 0), text, font=font, align="center", spacing=6)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = x1 + (x2 - x1 - tw) / 2
    y = y1 + (y2 - y1 - th) / 2
    draw.multiline_text((x, y), text, font=font, fill=fill, align="center", spacing=6)


def draw_box(draw: ImageDraw.ImageDraw, box, text, font, fill, outline=(51, 65, 85), width=3):
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=outline, width=width)
    center_text(draw, box, text, font)


def draw_arrow(draw: ImageDraw.ImageDraw, start, end, color=(6, 182, 212), width=8, head=18):
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=color, width=width)
    draw.polygon(
        [
            (x2, y2),
            (x2 - head, y2 - head // 2),
            (x2 - head, y2 + head // 2),
        ],
        fill=color,
    )


def main():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(img)

    title_font = load_font(68, bold=True)
    subtitle_font = load_font(36)
    label_font = load_font(40, bold=True)
    box_font = load_font(36)
    small_font = load_font(30)

    draw.text((80, 28), "Windows vs Linux 系統架構", font=title_font, fill=(15, 23, 42))
    draw.text((82, 112), "硬體 -> 作業系統 -> 系統分層", font=subtitle_font, fill=(71, 85, 105))

    draw.text((120, 190), "硬體", font=label_font, fill=(15, 23, 42))
    draw.text((610, 190), "作業系統", font=label_font, fill=(15, 23, 42))
    draw.text((1220, 190), "系統分層", font=label_font, fill=(15, 23, 42))

    cpu = (80, 270, 350, 390)
    ram = (80, 430, 350, 550)
    hdd = (80, 590, 350, 710)

    win = (560, 260, 980, 450)
    linux = (560, 500, 980, 750)

    app = (1140, 260, 1840, 410)
    util = (1140, 440, 1840, 560)
    kernel = (1140, 590, 1840, 710)
    hw = (1140, 740, 1840, 860)

    draw_box(draw, cpu, "CPU", box_font, (255, 255, 255))
    draw_box(draw, ram, "RAM", box_font, (255, 255, 255))
    draw_box(draw, hdd, "HDD", box_font, (255, 255, 255))

    draw_box(draw, win, "Windows\nC: / D:", box_font, (236, 254, 255), (6, 182, 212))
    draw_box(draw, linux, "Linux\n/ /home /etc /var", box_font, (240, 253, 244), (22, 163, 74))

    draw_box(draw, app, "Applications", box_font, (248, 250, 252))
    draw_box(draw, util, "OS Utilities", box_font, (248, 250, 252))
    draw_box(draw, kernel, "Kernel", box_font, (248, 250, 252))
    draw_box(draw, hw, "Hardware", box_font, (248, 250, 252))

    for y in (330, 490, 650):
        draw_arrow(draw, (350, y), (560, y), color=(100, 116, 139), width=5, head=14)

    draw_arrow(draw, (980, 340), (1140, 340), width=8, head=20)
    draw_arrow(draw, (980, 625), (1140, 500), width=8, head=20)

    draw.text((580, 790), "符合 FHS 標準規範", font=small_font, fill=(21, 128, 61))
    draw.line((770, 780, 730, 752), fill=(21, 128, 61), width=4)

    draw.text(
        (80, 930),
        "重點：Linux 使用單一目錄樹，常遵循 FHS。",
        font=small_font,
        fill=(30, 41, 59),
    )

    output = Path("image") / "Windows_Linux_學生版.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output)
    print(f"Generated: {output.resolve()}")


if __name__ == "__main__":
    main()
