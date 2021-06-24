class configSvcImpl:
    def __init__(self):
        self.protocol = "http"
        self.domain = "kiki.binacs.cn"

    def GetDomainSite(self):
        return self.protocol + "://" + self.domain