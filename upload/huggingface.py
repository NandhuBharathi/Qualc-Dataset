
from datasets import Dataset
from huggingface_hub import login
from kaggle_secrets import UserSecretsClient

from configs.config import REPO_ID


class HFUploader:

    def upload(self, data):

        secrets = UserSecretsClient()
        token = secrets.get_secret("HF_TOKEN")

        login(token=token)

        dataset = Dataset.from_list(data)
        dataset.push_to_hub(REPO_ID)

        print(f"Uploaded : {REPO_ID}")
