
import requests
from bs4 import BeautifulSoup


class WebCollector:

    def collect(self, config):

        url = config["url"]

        try:

            response = requests.get(url, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            paragraphs = []

            for p in soup.find_all("p"):

                text = p.get_text(" ", strip=True)

                if text:
                    paragraphs.append({"text": text})

            print(f"Collected : {url} ({len(paragraphs)})")

            return paragraphs

        except Exception as e:

            print(f"Failed : {url}")
            print(e)

            return []


    def collect_all(self, configs):

        datasets = []

        for config in configs:

            data = self.collect(config)

            if data:
                datasets.append(data)

        return datasets
