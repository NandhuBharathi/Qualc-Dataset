from collectors.huggingface import HFCollector
from preprocess.cleaner import Cleaner
from preprocess.filter import Filter
from preprocess.validator import Validator

collector = HFCollector()
cleaner = Cleaner()
dataset_filter = Filter()
validator = Validator()

dataset = collector.collect(
    dataset_name="ag_news",
    split="train[:10]"
)

cleaned = cleaner.process(dataset)
filtered = dataset_filter.process(cleaned)
validated = validator.process(filtered)

print(f"Cleaned: {len(cleaned)}")
print(f"Filtered: {len(filtered)}")
print(f"Validated: {len(validated)}")
print(validated[0])
