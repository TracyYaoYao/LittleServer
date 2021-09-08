import hashlib
from .configSvc import ConfigSvcImpl
from django.core.cache import cache
from .redisScv import CacheScvImpl
from django.utils import timezone
import time

class TinyurlSvcImpl:
    def __init__(self):
        self.INF = 0x3FFFFFFF
        self.MASK = 0x0000003D
        self.ALPHA = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encode(self, url):
        # 1. get md5 string
        hash = hashlib.md5()
        hash.update(url.encode())
        str = hash.hexdigest()
        # 2. generate 4 string
        res = []
        for i in range(4):
            byte = bytes(str[i * 8: (i + 1) * 8], 'UTF-8')
            hexv = int.from_bytes(byte, byteorder='big', signed=False)
            tmpv = self.INF & hexv
            turl = ""
            for _ in range(6):
                turl = turl + self.ALPHA[self.MASK & tmpv]
                tmpv = tmpv >> 5
            res.append(turl)
        # 3. return the first one. rand() is better.
        return res[0]

    def PasteEncode(self, content):
        content = content+timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        print(content)
        return self.encode(content)


    def EncodeURL(self, url):
        turl = self.encode(url)  # 把原始url压缩
        CacheScvImpl().CreateURLCache(turl, url)  # 写入redis
        return ConfigSvcImpl().GetDomainSite() + "/r/" + turl

    def DecodeURL(self, turl):
        return CacheScvImpl().SearchURL(turl[-6:])

    def SearchURL(self, turl):
        return CacheScvImpl().Get(turl[:])