from configs.datasets import DATASETS

from collectors.huggingface import HFCollector
from preprocess.cleaner import Cleaner
from preprocess.filter import Filter
from preprocess.validator import Validator
from exporters.parquet import ParquetExporter

collector = HFCollector()
cleaner = Cleaner()
dataset_filter = Filter()
validator = Validator()
exporter = ParquetExporter()

def main():

    for config in DATASETS:

        print(f"Processing : {config['name']}")

        dataset = collector.collect(
            dataset_name=config["name"],
            split=config["split"]
        )

        dataset = cleaner.process(dataset)
        dataset = dataset_filter.process(dataset)
        dataset = validator.process(dataset)

        output = exporter.export(dataset)

        print(f"Exported : {output}")

if __name__ == "__main__":
    main()
