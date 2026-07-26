
from configs.datasets import DATASETS
from configs.kaggle_datasets import KAGGLE_DATASETS
from configs.local_datasets import LOCAL_DATASETS
from configs.web_datasets import WEB_DATASETS


SOURCES = [

    {
        "type": "hf",
        "configs": DATASETS
    },

    {
        "type": "kaggle",
        "configs": KAGGLE_DATASETS
    },

    {
        "type": "local",
        "configs": LOCAL_DATASETS
    },

    {
        "type": "web",
        "configs": WEB_DATASETS
    }

]
