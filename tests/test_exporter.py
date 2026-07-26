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

dataset = collector.collect(
    dataset_name="ag_news",
    split="train[:10]"
)

dataset = cleaner.process(dataset)
dataset = dataset_filter.process(dataset)
dataset = validator.process(dataset)

output = exporter.export(dataset)

print(output)
