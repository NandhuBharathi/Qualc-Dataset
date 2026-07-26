
from collectors.hf_collector import HFCollector
from collectors.kaggle_collector import KaggleCollector
from collectors.local_collector import LocalCollector
from collectors.web_collector import WebCollector


class SourceManager:

    def __init__(self):

        self.collectors = {
            "hf": HFCollector(),
            "kaggle": KaggleCollector(),
            "local": LocalCollector(),
            "web": WebCollector(),
        }

    def collect(self, source_type, configs):

        collector = self.collectors.get(source_type)

        if collector is None:
            raise ValueError(f"Unknown source type: {source_type}")

        return collector.collect_all(configs)
