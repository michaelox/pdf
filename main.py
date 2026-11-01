import fitz  # PyMuPDF
import json

def parse_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        pages.append({
                            "text": span["text"],
                            "font_name": span["font"],
                            "font_size": span["size"],
                            "color": span["color"],
                            "bbox": span["bbox"],
                            "flags": span["flags"],
                            "page_num": page_num
                        })
    return pages

# Example usage
pdf_path = "original.pdf"
pages = parse_pdf(pdf_path)
print(json.dumps(pages, indent=2))

def match_font_and_style(span):
    font_name = span["font_name"]
    font_size = span["font_size"]
    color = span["color"]
    flags = span["flags"]
    bbox = span["bbox"]

    # Check if font is embedded
    if "BaseFont" in doc.get_font_info(span["font_name"]):
        font_file = doc.get_font_info(span["font_name"])["file"]
    else:
        # Map to closest Google Fonts or Adobe Fonts
        font_file = map_to_closest_font(font_name)

    return {
        "font_file": font_file,
        "font_size": font_size,
        "color": color,
        "flags": flags,
        "bbox": bbox
    }

def map_to_closest_font(font_name):
    # Logic to map to closest font
    return "closest-font.ttf"  # Placeholder
