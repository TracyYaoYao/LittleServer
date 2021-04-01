class configSvcImpl:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.protocol = "http"
        self.domain = "kiki.binacs.cn"

    def GetDomainSite(self):
        return self.protocol + "://" + self.domain
