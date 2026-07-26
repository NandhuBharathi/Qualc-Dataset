from collectors.downloader import PDFDownloader
from collectors.extractor import PDFExtractor

class LocalCollector:

    def __init__(self):
        self.downloader = PDFDownloader()
        self.extractor = PDFExtractor()

    def collect(self):
        url = ""  # PDF URL later

        if not url:
            return []

        pdf_path = self.downloader.download(url)
        text = self.extractor.extract(pdf_path)

        return [
            {
                "text": text
            }
        ]
