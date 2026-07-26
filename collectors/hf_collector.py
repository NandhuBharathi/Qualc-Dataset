
from datasets import load_dataset

class HFCollector:

    def collect(self, config):

        name = config["name"]
        subset = config.get("subset")
        split = config.get("split", "train")

        try:

            if subset:
                dataset = load_dataset(
                    path=name,
                    name=subset,
                    split=split
                )
            else:
                dataset = load_dataset(
                    path=name,
                    split=split
                )

            data = list(dataset)

            print(f"Collected : {name} ({len(data)})")

            return data

        except Exception as e:

            print(f"Failed : {name}")
            print(e)

            return []

    def collect_all(self, configs):

        datasets = []

        for config in configs:

            data = self.collect(config)

            if data:
                datasets.append(data)

        return datasets
