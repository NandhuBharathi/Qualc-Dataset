
import os
import json


class DatasetLoader:

    def __init__(self, input_dir="raw"):

        self.input_dir = input_dir

    def load(self):

        datasets = []

        if not os.path.exists(self.input_dir):
            return datasets

        for file in os.listdir(self.input_dir):

            if not file.endswith(".json"):
                continue

            path = os.path.join(self.input_dir, file)

            try:

                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                print(f"Loaded : {file} ({len(data)})")

                datasets.append(data)

            except Exception as e:

                print(f"Failed : {file}")
                print(e)

        return datasets
