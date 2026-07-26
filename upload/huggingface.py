from datasets import load_dataset
from configs.config import REPO_ID

class HuggingFaceUploader:

    def upload(self, dataset):
        dataset.push_to_hub(REPO_ID)
