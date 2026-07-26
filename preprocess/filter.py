class Filter:

    def process(self, dataset):
        filtered = []
        seen = set()

        for row in dataset:
            text = row.get("text", "")

            if text in seen:
                continue

            seen.add(text)
            filtered.append(row)

        return filtered
