from pathlib import Path

import aspose.slides as slides


def convert_pptx_to_png(pptx_path: Path) -> tuple[int, Path]:
    output_dir = pptx_path.parent / f"{pptx_path.stem}_images"
    output_dir.mkdir(parents=True, exist_ok=True)

    with slides.Presentation(str(pptx_path)) as pres:
        slide_count = len(pres.slides)
        for idx, sld in enumerate(pres.slides, start=1):
            with sld.get_image(2.0, 2.0) as img:
                out_file = output_dir / f"slide_{idx:02d}.png"
                img.save(str(out_file), slides.ImageFormat.PNG)

    return slide_count, output_dir


def main() -> None:
    root = Path(__file__).resolve().parents[1] / "PPT"
    if not root.exists():
        raise FileNotFoundError(f"PPT folder not found: {root}")

    files = sorted(
        p for p in root.glob("*.pptx")
        if not p.name.startswith("~$")
    )
    if not files:
        print("No .pptx files found.")
        return

    for pptx_file in files:
        try:
            count, out_dir = convert_pptx_to_png(pptx_file)
            print(f"Converted: {pptx_file.name} -> {out_dir.name} ({count} slides)")
        except Exception as exc:
            print(f"Skipped: {pptx_file.name} ({exc})")


if __name__ == "__main__":
    main()
