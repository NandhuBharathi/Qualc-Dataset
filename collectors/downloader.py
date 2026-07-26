import os
import requests

class PDFDownloader:

    def download(self, url, output_dir="downloads"):
        os.makedirs(output_dir, exist_ok=True)

        filename = os.path.join(output_dir, url.split("/")[-1])

        response = requests.get(url, timeout=60)
        response.raise_for_status()

        with open(filename, "wb") as f:
            f.write(response.content)

        return filename
