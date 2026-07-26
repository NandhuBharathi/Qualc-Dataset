from datasets import load_dataset

class HFCollector:

    def collect(self, dataset_name, split="train"):
        dataset = load_dataset(dataset_name, split=split)
        return dataset
