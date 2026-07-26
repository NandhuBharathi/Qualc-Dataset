
class Statistics:

    def process(self, original, cleaned, deduplicated, validated):

        print("\n========== PIPELINE STATS ==========")

        print(f"Original      : {original}")
        print(f"Cleaned       : {cleaned}")
        print(f"Deduplicated  : {deduplicated}")
        print(f"Validated     : {validated}")

        if original:

            print(f"\nRetention     : {(validated / original) * 100:.2f}%")

        print("====================================")
