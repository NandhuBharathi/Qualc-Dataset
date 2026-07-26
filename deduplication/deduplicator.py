
import hashlib


class Deduplicator:

    def process(self, dataset):

        unique = []
        seen = set()

        for row in dataset:

            key = self.make_key(row)

            if key not in seen:
                seen.add(key)
                unique.append(row)

        return unique


    def make_key(self, row):

        if "text" in row:
            value = row["text"]

        elif "instruction" in row:
            value = (
                row.get("instruction", "")
                + row.get("input", "")
                + row.get("output", "")
            )

        elif "code" in row:
            value = row["code"]

        else:
            value = str(row)

        return hashlib.sha256(
            value.strip().lower().encode("utf-8")
        ).hexdigest()
