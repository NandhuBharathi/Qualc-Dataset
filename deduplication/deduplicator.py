class Deduplicator:

    def process(self, dataset):
        unique = []
        seen = set()

        for row in dataset:
            text = row.get("text", "").strip()

            if text in seen:
                continue

            seen.add(text)
            unique.append(row)

        return unique
