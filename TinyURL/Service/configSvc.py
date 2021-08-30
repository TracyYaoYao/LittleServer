class ConfigSvcImpl:
    def __init__(self):
        self.protocol = "https"
        self.domain = "kiki.zone"
        # self.protocol_dev = "http"
        # self.domain_dev = "127.0.0.1:8006"

    def GetDomainSite(self):
        return self.protocol + "://" + self.domain

        # return self.protocol_dev + "://" + self.domain_dev