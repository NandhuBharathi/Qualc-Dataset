
import os
import json


class DatasetDownloader:

    def __init__(self, output_dir="raw"):

        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def save(self, name, dataset):

        filename = (
            name.replace("/", "_")
                .replace(":", "_")
                .replace(" ", "_")
            + ".json"
        )

        path = os.path.join(self.output_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                dataset,
                f,
                ensure_ascii=False,
                indent=2
            )

        print(f"Saved : {path}")

        return path
