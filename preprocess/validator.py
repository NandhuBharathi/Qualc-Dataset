class Validator:

    def process(self, dataset):
        validated = []

        for row in dataset:
            text = row.get("text", "")

            if not isinstance(text, str):
                continue

            if len(text) < 20:
                continue

            validated.append(row)

        return validated
