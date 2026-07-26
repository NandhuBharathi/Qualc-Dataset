from collectors.huggingface import HFCollector

collector = HFCollector()

dataset = collector.collect(
    dataset_name="ag_news",
    split="train[:5]"
)

print(dataset)
print(dataset[0])
