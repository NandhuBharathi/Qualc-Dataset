
from collections import Counter


class DatasetAnalyzer:

    def analyze(self, dataset):

        total = len(dataset)

        keys = Counter()

        lengths = []

        for item in dataset:

            keys.update(item.keys())

            if "text" in item:
                lengths.append(len(item["text"]))

            elif "instruction" in item:
                lengths.append(len(item["instruction"]))

        print("=" * 40)
        print(f"Total Records : {total}")
        print()

        print("Fields:")

        for key, count in keys.items():
            print(f"{key:15} {count}")

        if lengths:
            print()
            print(f"Min Length : {min(lengths)}")
            print(f"Max Length : {max(lengths)}")
            print(f"Average    : {sum(lengths)/len(lengths):.2f}")

        print("=" * 40)
