from pathlib import Path
from shutil import copy2
from zipfile import ZipFile

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph


SRC = Path(r"E:\Download\[PK]战斗表现-规则框架（含部分示意图）V-0.1.docx")
TARGET_DOCX = Path(r"E:\PK\设计文档\自动战斗表现框架v0.3-模块结构版-含流程图.docx")
TARGET_MD = Path(r"E:\PK\设计文档\自动战斗表现框架v0.3-模块结构版-含流程图.md")
COPY_DOCX = Path(r"E:\PK\设计文档\自动战斗表现框架v0.4-规则框架同步版.docx")
COPY_MD = Path(r"E:\PK\设计文档\自动战斗表现框架v0.4-规则框架同步版.md")
MEDIA_DIR = Path(r"E:\PK\设计文档\_source_pk_framework_images")


def iter_block_items(parent):
    parent_elm = parent.element.body if hasattr(parent, "element") else parent._tc
    for child in parent_elm.iterchildren():
        if child.tag.endswith("}p"):
            yield Paragraph(child, parent)
        elif child.tag.endswith("}tbl"):
            yield Table(child, parent)


def cell_text(cell):
    return " ".join(p.text.strip().replace("\n", " ") for p in cell.paragraphs if p.text.strip())


def escape_table(text):
    return text.replace("|", "\\|").replace("\n", " ")


def image_rel_ids(paragraph):
    rel_ids = []
    for blip in paragraph._p.xpath(".//*[local-name()='blip']"):
        rid = blip.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
        if rid:
            rel_ids.append(rid)
    return rel_ids


def extract_media(doc):
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)
    rid_to_file = {}
    index = 0
    for rid, rel in doc.part.rels.items():
        if "image" not in rel.reltype:
            continue
        index += 1
        content_type = rel.target_part.content_type
        ext = {
            "image/png": ".png",
            "image/jpeg": ".jpeg",
            "image/jpg": ".jpg",
        }.get(content_type, Path(rel.target_ref).suffix or ".img")
        out = MEDIA_DIR / f"doc_image_{index:02d}{ext}"
        out.write_bytes(rel.target_part.blob)
        rid_to_file[rid] = out
    return rid_to_file


def table_to_md(table):
    rows = [[escape_table(cell_text(cell)) for cell in row.cells] for row in table.rows]
    if not rows:
        return []
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    lines = []
    lines.append("| " + " | ".join(rows[0]) + " |")
    lines.append("| " + " | ".join(["---"] * width) + " |")
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def build_markdown():
    doc = Document(SRC)
    rid_to_file = extract_media(doc)
    lines = []
    first_text = True
    image_count = 0

    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            text = block.text.strip()
            rel_ids = image_rel_ids(block)

            if text:
                if first_text:
                    lines.append(f"# {text}")
                    first_text = False
                else:
                    lines.append(text)
                lines.append("")

            for rid in rel_ids:
                image_count += 1
                img = rid_to_file.get(rid)
                if img:
                    rel_path = img.relative_to(Path(r"E:\PK"))
                    lines.append(f"![图示{image_count}](../{rel_path.as_posix().replace('设计文档/', '设计文档/')})")
                else:
                    lines.append(f"![图示{image_count}]()")
                lines.append("")

        elif isinstance(block, Table):
            lines.extend(table_to_md(block))
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    TARGET_DOCX.parent.mkdir(parents=True, exist_ok=True)
    copy2(SRC, TARGET_DOCX)
    copy2(SRC, COPY_DOCX)

    md = build_markdown()
    TARGET_MD.write_text(md, encoding="utf-8")
    COPY_MD.write_text(md, encoding="utf-8")

    print(TARGET_DOCX)
    print(TARGET_MD)
    print(COPY_DOCX)
    print(COPY_MD)


if __name__ == "__main__":
    main()
