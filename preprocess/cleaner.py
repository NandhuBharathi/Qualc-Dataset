class Cleaner:

    def process(self, dataset):
        cleaned = []

        for row in dataset:
            text = row.get("text", "")

            if not isinstance(text, str):
                continue

            text = text.strip()

            if not text:
                continue

            cleaned.append({
                "text": text
            })

        return cleaned
