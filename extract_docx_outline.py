from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph


SRC = Path(r"E:\Download\[PK]战斗表现-规则框架（含部分示意图）V-0.1.docx")
OUT = Path(r"E:\PK\设计文档\_source_pk_combat_framework_extract.md")


def iter_block_items(parent):
    if hasattr(parent, "element") and parent.element.body is not None:
        parent_elm = parent.element.body
    else:
        parent_elm = parent._tc
    for child in parent_elm.iterchildren():
        if child.tag.endswith("}p"):
            yield Paragraph(child, parent)
        elif child.tag.endswith("}tbl"):
            yield Table(child, parent)


def cell_text(cell):
    return " ".join(p.text.strip().replace("\n", " ") for p in cell.paragraphs if p.text.strip())


def main():
    doc = Document(SRC)
    lines = [f"# Extract: {SRC.name}", ""]
    table_i = 0
    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            text = block.text.strip()
            if not text:
                continue
            style = block.style.name if block.style is not None else ""
            if style.startswith("Heading"):
                try:
                    level = int(style.split()[-1])
                except Exception:
                    level = 2
                lines.append(f"{'#' * min(level + 1, 6)} {text}")
            else:
                lines.append(text)
            lines.append("")
        elif isinstance(block, Table):
            table_i += 1
            rows = [[cell_text(cell) for cell in row.cells] for row in block.rows]
            lines.append(f"<!-- TABLE {table_i} -->")
            if rows:
                width = max(len(r) for r in rows)
                norm = [r + [""] * (width - len(r)) for r in rows]
                lines.append("| " + " | ".join(norm[0]) + " |")
                lines.append("| " + " | ".join(["---"] * width) + " |")
                for row in norm[1:]:
                    lines.append("| " + " | ".join(row) + " |")
            lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
