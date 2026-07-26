
from collections import Counter


class Verifier:

    def show(self, dataset):

        print("\n========== DATASET REPORT ==========")

        total = len(dataset)

        print(f"Total Records : {total}")

        counter = Counter()

        empty = 0

        for row in dataset:

            if not row:
                empty += 1
                continue

            if "instruction" in row:
                counter["instruction"] += 1

            elif "text" in row:
                counter["text"] += 1

            elif "code" in row:
                counter["code"] += 1

            else:
                counter["other"] += 1

        print()

        for key in sorted(counter):

            count = counter[key]
            percent = (count / total * 100) if total else 0

            print(f"{key:<15}: {count:>10} ({percent:.2f}%)")

        print(f"\nEmpty Records : {empty}")

        print("\n====================================")
