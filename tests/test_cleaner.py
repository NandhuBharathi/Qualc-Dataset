from collectors.huggingface import HFCollector
from preprocess.cleaner import Cleaner

collector = HFCollector()
cleaner = Cleaner()

dataset = collector.collect(
    dataset_name="ag_news",
    split="train[:5]"
)

cleaned = cleaner.process(dataset)

print(cleaned[0])
print(len(cleaned))
