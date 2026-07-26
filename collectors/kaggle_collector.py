
import kagglehub
import os

class KaggleCollector:

    def collect(self, config):

        dataset = config["dataset"]

        try:

            path = kagglehub.dataset_download(dataset)

            print(f"Downloaded : {dataset}")
            print(f"Location   : {path}")

            return path

        except Exception as e:

            print(f"Failed : {dataset}")
            print(e)

            return None

    def collect_all(self, configs):

        paths = []

        for config in configs:

            path = self.collect(config)

            if path:
                paths.append(path)

        return paths
