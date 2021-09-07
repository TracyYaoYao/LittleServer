import unittest
from HTMLTestRunner import HTMLTestRunner
import requests
from parameterized import parameterized
import ddt
from BSTestRunner import BSTestRunner

svc_name = ['tinyurl', 'pastebin', 'filesave']

svc_prod_api = {'tinyurl': 'https://kiki.zone/api/tinyurl/encode',
           'pastebin': 'https://kiki.zone/api/pastebin/submit',
           'filesave': 'https://kiki.zone/api/filesave/put'}


svc_dev_api = {'tinyurl': 'http://127.0.0.1:8006/api/tinyurl/encode',
                'pastebin': 'http://127.0.0.1:8006/api/pastebin/submit',
                'filesave': 'http://127.0.0.1:8006/api/filesave/put'}

@ddt.dtt
class TinyURLTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('tinyurl cases start here')

    @classmethod
    def tearDownClass(cls):
        print('tests end')
        pass


    # @parameterized.expand([
    #     ('tinyURL: None-url', svc_prod_api[svc_name[0]], {'surl': ''}, '"ERROR: blank url..."'),
    #     ('tinyURL: Err-url',svc_prod_api[svc_name[0]], {'surl': 'http123'}, '"ERROR: url must be started with http:/https:"'),
    #     ('tinyURL: http-url',svc_prod_api[svc_name[0]], {'surl': 'http://binacs.cn'}, "https://kiki.zone/r/BVniuy"),
    #     ('tinyURL: https-url',svc_prod_api[svc_name[0]], {'surl': 'https://binacs.cn'}, "https://kiki.zone/r/6VniAr"),
    #
    # ])

    test_data = [
        {},

    ]



    def testTinyUrl(self, name, svc_api, data, assert_title):
        # print('url is null')
        requests.packages.urllib3.disable_warnings()
        r = requests.post(svc_api, data=data, verify=False)
        print(r.text)
        self.assertEqual(r.text, assert_title)

    @ddt.data(*test_data)
    def testPasteBin(self, value):
        requests.packages.urllib3.disable_warnings()
        r = requests.post(svc_prod_api[svc_name[0]], data=value, verify=False)
        print(r.text)
        self.assertEqual(r.text, '1')



    # def test_errUrl(self,name, svc_api, data, assert_title):
    #     print('url is error')
    #     requests.packages.urllib3.disable_warnings()
    #     r = requests.post(svc_api, data=data, verify=False)
    #     print(r.text)
    #     self.assertEqual(r.text, assert_title)
    #
    # def testNormalUrl(self,name, svc_api, data, assert_title):
    #     print('http normal')
    #     requests.packages.urllib3.disable_warnings()
    #     r = requests.post(svc_api, data=data, verify=False)
    #     print(r.text)
    #     self.assertEqual(r.text, assert_title)
    #
    # def testNormalUrl(self,name, svc_api, data, assert_title):
    #     print('https normal')
    #     requests.packages.urllib3.disable_warnings()
    #     r = requests.post(svc_api, data=data, verify=False)
    #     print(r.text)
    #     self.assertEqual(r.text, assert_title)




if __name__ == '__main__':
    unittest.main(verbosity=2)
