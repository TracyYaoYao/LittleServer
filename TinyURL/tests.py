from django.test import TestCase

import unittest
import HTMLTestRunner
import requests
from parameterized import parameterized
import time


svc_name = ['tinyurl', 'pastebin', 'filesave']

svc_prod_api = {'tinyurl': 'https://kiki.zone/api/tinyurl/encode',
           'pastebin': 'https://kiki.zone/api/pastebin/submit',
           'filesave': 'https://kiki.zone/api/filesave/put'}


svc_dev_api = {'tinyurl': 'http://127.0.0.1:8006/api/tinyurl/encode',
                'pastebin': 'http://127.0.0.1:8006/api/pastebin/submit',
                'filesave': 'http://127.0.0.1:8006/api/filesave/put'}


class TinyURLTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('tinyurl cases start here')

    @classmethod
    def tearDownClass(cls):
        print('tests end')


    @parameterized.expand([
        ('tinyURL: None-url', svc_prod_api[svc_name[0]], {'surl': ''}, '"ERROR: blank url..."'),
        ('tinyURL: Err-url',svc_prod_api[svc_name[0]], {'surl': 'http123'}, '"ERROR: url must be started with http:/https:"'),
        ('tinyURL: http-url',svc_prod_api[svc_name[0]], {'surl': 'http://binacs.cn'}, "https://kiki.zone/r/BVniuy"),
        ('tinyURL: https-url',svc_prod_api[svc_name[0]], {'surl': 'https://binacs.cn'}, "https://kiki.zone/r/6VniAr"),

    ])


    def testTinyUrl(self, name, svc_api, data, assert_title):
        requests.packages.urllib3.disable_warnings()
        r = requests.post(svc_api, data=data, verify=False)
        print(r.text)
        self.assertEqual(r.text, assert_title)

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(now)
    testunit = unittest.TestSuite()
    testunit.addTest(TinyURLTest("testTinyUrl"))
    HtmlFile = "test_report.html"

    fp = open(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度测试报告", description=u"用例测试情况")
    runner.run(testunit)
    fp.close()


    # unittest.main(verbosity=2)
