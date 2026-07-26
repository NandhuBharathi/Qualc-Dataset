from datasets import Dataset

class ParquetExporter:

    def export(self, dataset):
        hf_dataset = Dataset.from_list(dataset)
        hf_dataset.to_parquet("dataset.parquet")
        return "dataset.parquet"
