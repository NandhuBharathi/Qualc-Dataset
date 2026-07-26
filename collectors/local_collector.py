
import os
import json
import pandas as pd


class LocalCollector:

    def collect(self, config):

        path = config["path"]

        if not os.path.exists(path):
            print(f"File not found: {path}")
            return []

        ext = os.path.splitext(path)[1].lower()

        try:

            if ext == ".json":
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)

            elif ext == ".jsonl":
                with open(path, "r", encoding="utf-8") as f:
                    data = [json.loads(line) for line in f]

            elif ext == ".csv":
                data = pd.read_csv(path).to_dict("records")

            elif ext == ".parquet":
                data = pd.read_parquet(path).to_dict("records")

            elif ext == ".txt":
                with open(path, "r", encoding="utf-8") as f:
                    data = [{"text": line.strip()} for line in f if line.strip()]

            else:
                print(f"Unsupported file type: {ext}")
                return []

            print(f"Collected: {path} ({len(data)})")
            return data

        except Exception as e:
            print(f"Failed: {path}")
            print(e)
            return []

    def collect_all(self, configs):

        datasets = []

        for config in configs:
            data = self.collect(config)

            if data:
                datasets.append(data)

        return datasets
