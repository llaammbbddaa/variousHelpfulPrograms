import os
from pypdf import PdfReader, PdfWriter

# ——— CONFIG ———
INPUT_DIR        = "/home/mouse/Documents/macPdfs/qT/"  # directory containing all your PDFs
OUTPUT_PREFIX    = "combined"                 # will generate combined_1.pdf, combined_2.pdf, …
PAGES_PER_FILE   = 50
# ——————————

def get_pdf_paths(input_dir):
    # Grab all .pdf files, sorted alphabetically
    return sorted(
        os.path.join(input_dir, f)
        for f in os.listdir(input_dir)
        if f.lower().endswith(".pdf")
    )

def batch_combine(input_dir, output_prefix, pages_per_file):
    pdf_paths = get_pdf_paths(input_dir)
    writer = PdfWriter()
    file_count = 1
    page_count = 0

    for pdf_path in pdf_paths:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)
            page_count += 1

            # once we hit the threshold, write out and reset
            if page_count >= pages_per_file:
                out_name = f"{output_prefix}_{file_count}.pdf"
                with open(out_name, "wb") as out_f:
                    writer.write(out_f)
                print(f"Wrote {out_name} ({page_count} pages)")

                # reset
                file_count += 1
                writer = PdfWriter()
                page_count = 0

    # write remaining pages, if any
    if page_count > 0:
        out_name = f"{output_prefix}_{file_count}.pdf"
        with open(out_name, "wb") as out_f:
            writer.write(out_f)
        print(f"Wrote {out_name} ({page_count} pages)")

if __name__ == "__main__":
    batch_combine(INPUT_DIR, OUTPUT_PREFIX, PAGES_PER_FILE)
