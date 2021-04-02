from flightsparser.cache import LocalCache
import pathlib
import os


class TestLocalCache:
    def test_get_cache_elements_empty(self):
        cache = LocalCache()
        cache.cache_path = f"{pathlib.Path(__file__).parent.absolute()}/local_cache.pkl"
        cache.remove_cache()
        elements = cache.get_cache_elements()
        assert isinstance(elements, list)
        assert elements == []

    def test_add_cache(self):
        cache = LocalCache()
        cache.cache_path = f"{pathlib.Path(__file__).parent.absolute()}/local_cache.pkl"
        cache.remove_cache()
        cache.add_element("aaaa", [123, 4354, 54545])
        elements = cache.get_cache_elements()
        assert isinstance(elements, list)
        assert elements == ["aaaa"]
        cache.add_element("bbbb", [23243, 45354, 5454545])
        elements = cache.get_cache_elements()
        assert isinstance(elements, list)
        assert elements == ["aaaa", "bbbb"]

    def test_get_element(self):
        cache = LocalCache()
        cache.cache_path = f"{pathlib.Path(__file__).parent.absolute()}/local_cache.pkl"
        data = cache.get_element("ssdsd")
        assert data == []
        data = cache.get_element("aaaa")
        assert data == [123, 4354, 54545]

    def test_remove_cache(self):
        cache = LocalCache()
        cache.cache_path = f"{pathlib.Path(__file__).parent.absolute()}/local_cache.pkl"
        cache.remove_cache()
        assert os.path.exists(cache.cache_path) is False


class TestRedisCache:
    def test_get_cache_elements_empty(self):
        cache = LocalCache()
        cache.cache_path = f"{pathlib.Path(__file__).parent.absolute()}/local_cache.pkl"
        cache.remove_cache()
        elements = cache.get_cache_elements()
        assert isinstance(elements, list)
        assert elements == []

    def test_add_cache(self):
        cache = LocalCache()
        cache.cache_path = f"{pathlib.Path(__file__).parent.absolute()}/local_cache.pkl"
        cache.remove_cache()
        cache.add_element("aaaa", [123, 4354, 54545])
        elements = cache.get_cache_elements()
        assert isinstance(elements, list)
        assert elements == ["aaaa"]
        cache.add_element("bbbb", [23243, 45354, 5454545])
        elements = cache.get_cache_elements()
        assert isinstance(elements, list)
        assert elements == ["aaaa", "bbbb"]

    def test_get_element(self):
        cache = LocalCache()
        cache.cache_path = f"{pathlib.Path(__file__).parent.absolute()}/local_cache.pkl"
        data = cache.get_element("ssdsd")
        assert data == []
        data = cache.get_element("aaaa")
        assert data == [123, 4354, 54545]

    def test_remove_cache(self):
        cache = LocalCache()
        cache.cache_path = f"{pathlib.Path(__file__).parent.absolute()}/local_cache.pkl"
        cache.remove_cache()
        assert os.path.exists(cache.cache_path) is False
