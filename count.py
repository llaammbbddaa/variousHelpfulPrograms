import os
from pypdf import PdfReader

def total_pages_in_directory(pdf_dir):
    total = 0
    for fname in os.listdir(pdf_dir):
        if not fname.lower().endswith('.pdf'):
            continue
        path = os.path.join(pdf_dir, fname)
        try:
            reader = PdfReader(path)
            num = len(reader.pages)
            print(f"{fname}: {num} pages")
            total += num
        except Exception as e:
            print(f"Error reading {fname}: {e}")
    return total

if __name__ == "__main__":
    directory = "/home/mouse/Documents/macPdfs/qT/"
    total = total_pages_in_directory(directory)
    print(f"\nTotal pages across all PDFs: {total}")
