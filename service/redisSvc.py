import redis

class redisSvcImpl:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.cli = redis.Redis(host='localhost', port=6379, password='password', decode_responses=True)
    
    def Set(self, turl, url):
        self.cli.set(turl, url)
    
    def Get(self, turl):
        return self.cli.get(turl)
