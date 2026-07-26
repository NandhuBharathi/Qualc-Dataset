
class Merger:

    def process(self, datasets):

        merged = []

        for dataset in datasets:

            if not dataset:
                continue

            merged.extend(dataset)

        print(f"Merged : {len(merged)}")

        return merged
