class configSvcImpl:
    def __init__(self):
        self.protocol = "http"
        self.domain = "kiki.zone"
        # self.domain = "127.0.0.1:8000"

    def GetDomainSite(self):
        return self.protocol + "://" + self.domain