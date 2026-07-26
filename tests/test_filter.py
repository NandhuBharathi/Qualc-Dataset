from collectors.huggingface import HFCollector
from preprocess.cleaner import Cleaner
from preprocess.filter import Filter

collector = HFCollector()
cleaner = Cleaner()
dataset_filter = Filter()

dataset = collector.collect(
    dataset_name="ag_news",
    split="train[:10]"
)

cleaned = cleaner.process(dataset)
filtered = dataset_filter.process(cleaned)

print(f"Cleaned: {len(cleaned)}")
print(f"Filtered: {len(filtered)}")
