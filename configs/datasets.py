
DATASETS = [

    # General Knowledge
    {
        "name": "wikimedia/wikipedia",
        "subset": "20231101.en",
        "split": "train"
    },
    {
        "name": "Salesforce/wikitext",
        "subset": "wikitext-103-v1",
        "split": "train"
    },

    # News
    {
        "name": "ag_news",
        "split": "train"
    },

    # Reviews
    {
        "name": "imdb",
        "split": "train"
    },

    # Question Answering
    {
        "name": "squad",
        "split": "train"
    },
    {
        "name": "google/boolq",
        "split": "train"
    },

    # Instruction
    {
        "name": "databricks/databricks-dolly-15k",
        "split": "train"
    },

    # Mathematics
    {
        "name": "openai/gsm8k",
        "subset": "main",
        "split": "train"
    },

    # Commonsense Reasoning
    {
        "name": "allenai/ai2_arc",
        "subset": "ARC-Challenge",
        "split": "train"
    },

    # Science QA
    {
        "name": "allenai/openbookqa",
        "subset": "main",
        "split": "train"
    }
]
