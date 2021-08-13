from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos import CosClientError

import sys, os
import logging
import time
import requests
from urllib.parse import quote_plus
from LittleServer.settings.prod import secret_id, secret_key

logging.basicConfig(level=logging.INFO, stream=sys.stdout)



region = 'ap-guangzhou'  # 替换为用户的region
# token = None   # 使用临时密钥需要传入Token，默认为空,可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)  # 获取配置对象
client = CosS3Client(config)



class Upload():
    def upload(self, localFile):    # 文件流 简单上传
        response = client.list_buckets()
        name = localFile.name.split('.')
        t = time.strftime("%Y-%m-%d %X", time.localtime())
        url_s = name[0] + '%' + t + '.' + name[1]
        url_key = quote_plus(url_s.encode('utf-8'))

        response = client.put_object(
            Bucket = "tracy-1253239487",  # Bucket由bucketname-appid组成
            Body = localFile,  # 上传的文件
            Key = url_key,
            StorageClass = 'STANDARD',
            ContentType = 'text/html; charset=utf-8'
        )
        return config.uri("tracy-1253239487", url_key)
