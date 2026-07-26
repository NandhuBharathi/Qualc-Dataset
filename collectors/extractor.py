import fitz  # PyMuPDF

class PDFExtractor:

    def extract(self, pdf_path):
        text = []

        with fitz.open(pdf_path) as pdf:
            for page in pdf:
                text.append(page.get_text())

        return "\n".join(text)
