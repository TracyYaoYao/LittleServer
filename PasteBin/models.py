from django.db import models
import datetime
from django.utils import timezone

class Paste(models.Model):
    id = models.AutoField(primary_key=True)   #指定主键，如果不指定，MySQL会自动创建一个
    poster = models.CharField(max_length=30)
    content = models.TextField()    # max paste size is 4kb
    syntax = models.CharField(max_length=30)  # 目前只支持markdown语法，这一行数据暂时不起作用
    TinyURL = models.URLField()
    createTime = models.DateTimeField()

    def __str__(self):
        return self.poster