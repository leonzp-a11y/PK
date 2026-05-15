from pathlib import Path
from zipfile import ZipFile


SRC = Path(r"E:\Download\[PK]战斗表现-规则框架（含部分示意图）V-0.1.docx")
OUT_DIR = Path(r"E:\PK\设计文档\_source_pk_framework_images")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with ZipFile(SRC) as zf:
        names = [n for n in zf.namelist() if n.startswith("word/media/")]
        for i, name in enumerate(names, 1):
            ext = Path(name).suffix.lower()
            out = OUT_DIR / f"image_{i:02d}{ext}"
            out.write_bytes(zf.read(name))
            print(out)


if __name__ == "__main__":
    main()
