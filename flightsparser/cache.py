from typing import Dict, List
from flightsparser import CACHE_PATH, REDIS_HOST, REDIS_PORT, EXPIRATION_TIME_SECONDS
import pickle
import os
import redis


class LocalCache:
    def __init__(self) -> None:
        self.cache_path = CACHE_PATH

    def get_cache_elements(self) -> List:
        current_data = self.__read_cache()
        if isinstance(current_data, dict):
            keys = current_data.keys()
            return list(keys)
        return []

    def get_element(self, key: str) -> List:
        current_data = self.__read_cache()
        data = current_data.get(key, [])
        return data

    def add_element(self, key: str, data: List) -> None:
        current_data = self.__read_cache()
        if key not in current_data:
            current_data[key] = data
            self.__write_cache(current_data)

    def remove_cache(self) -> None:
        if os.path.exists(self.cache_path):
            os.remove(self.cache_path)

    def __write_cache(self, data):
        with open(self.cache_path, "wb") as cache_file:
            pickle.dump(data, cache_file)

    def __read_cache(self) -> Dict:
        if os.path.exists(self.cache_path):
            with open(self.cache_path, "rb") as cache_file:
                data = pickle.load(cache_file)
            return data
        return {}


class RedisCache:
    def __init__(self) -> None:
        self.host = REDIS_HOST
        self.port = REDIS_PORT
        self.expiration_time_seconds = EXPIRATION_TIME_SECONDS
        self.redis_client = redis.Redis(host=self.host, port=self.port)

    def get_cache_elements(self) -> List:
        pass

    def get_element(self, key: str) -> List:
        redis_data = self.redis_client.get(key)
        return pickle.loads(redis_data)

    def add_element(self, key: str, data: List) -> None:
        redis_data = pickle.dumps(data)
        self.redis_client.set(key, redis_data, ex=self.expiration_time_seconds)
