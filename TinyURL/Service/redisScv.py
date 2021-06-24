from django.core.cache import cache

class CacheScv():
    def CreateURLCache(self, turl, url):
        cache.set(turl, url, timeout=None)  # 永不超时

    def SearchURL(self, turl):
        return cache.get(turl[:])  # 从redis缓存中读取数据 找到编码后对应的原始url


