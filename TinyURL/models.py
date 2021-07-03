from django.db import models

# Create your models here.


class TinyURL(models.Model):
    id = models.AutoField(primary_key=True)   #指定主键，如果不指定，MySQL会自动创建一个
    surl = models.URLField()   # 不会去访问该url 验证是否正确
    tinyurl = models.URLField()

    def __str__(self):
        return self.id