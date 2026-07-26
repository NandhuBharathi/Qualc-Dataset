
import os
import pickle


class CacheManager:

    def __init__(self, cache_dir="cache"):

        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def _path(self, key):

        filename = key.replace("/", "_").replace(":", "_")
        return os.path.join(self.cache_dir, f"{filename}.pkl")

    def exists(self, key):

        return os.path.exists(self._path(key))

    def load(self, key):

        with open(self._path(key), "rb") as f:
            return pickle.load(f)

    def save(self, key, data):

        with open(self._path(key), "wb") as f:
            pickle.dump(data, f)

    def clear(self):

        for file in os.listdir(self.cache_dir):

            if file.endswith(".pkl"):
                os.remove(os.path.join(self.cache_dir, file))
