class Statistics:

    def show(self, original, cleaned, deduplicated, validated):
        print("\n========== DATASET REPORT ==========")
        print(f"Original      : {original}")
        print(f"Cleaned       : {cleaned}")
        print(f"Deduplicated  : {deduplicated}")
        print(f"Validated     : {validated}")
        print("====================================\n")
