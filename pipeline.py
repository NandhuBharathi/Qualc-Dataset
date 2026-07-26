
from collectors.source_manager import SourceManager
from configs.sources import SOURCES

from preprocess.cleaner import Cleaner
from preprocess.validator import Validator
from deduplication.deduplicator import Deduplicator
from formatters.formatter import Formatter
from merge.merger import Merger
from verify.verify import Verifier
from exporters.parquet_exporter import ParquetExporter
from upload.hf_uploader import HFUploader


manager = SourceManager()

cleaner = Cleaner()
validator = Validator()
deduplicator = Deduplicator()
formatter = Formatter()
merger = Merger()
verifier = Verifier()
exporter = ParquetExporter()
uploader = HFUploader()


processed = []


for source in SOURCES:

    datasets = manager.collect(
        source["type"],
        source["configs"]
    )

    for dataset in datasets:

        dataset = cleaner.process(dataset)
        dataset = validator.process(dataset)
        dataset = deduplicator.process(dataset)
        dataset = formatter.process(dataset)

        processed.append(dataset)


merged = merger.process(processed)

verifier.show(merged)

exporter.export(
    merged,
    "qualc_mark1.parquet"
)

uploader.upload(merged)

print("Qualc Dataset Pipeline Completed Successfully.")
