
import json
import os


class DatasetRegistry:

    def __init__(self, filename="dataset_registry.json"):

        self.filename = filename

        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                self.registry = json.load(f)
        else:
            self.registry = {}

    def add(self, name, records, source):

        self.registry[name] = {
            "records": records,
            "source": source
        }

        self.save()

    def exists(self, name):

        return name in self.registry

    def get(self, name):

        return self.registry.get(name)

    def save(self):

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(
                self.registry,
                f,
                indent=4,
                ensure_ascii=False
            )

    def show(self):

        for name, info in self.registry.items():
            print(
                f"{name} | {info['source']} | {info['records']} records"
            )
