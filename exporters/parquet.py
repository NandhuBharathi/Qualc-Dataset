
from datasets import Dataset


class ParquetExporter:

    def export(self, dataset, filename="dataset.parquet"):

        hf_dataset = Dataset.from_list(dataset)

        hf_dataset.to_parquet(filename)

        print(f"Exported : {filename}")

        return filename
