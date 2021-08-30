from .base import *

DEBUG = True

print('in prod')


ALLOWED_HOSTS = ['*']



# 1. 先配置环境包
# 2. 把redis作为Django的缓存设置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis_dc:6379",   # 在docker容器里 可以直连接。所以只需要写redis容器的名称和port
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "PASSWORD": "password",
        }
    }
}
#
# # 3.设置redis存储django的session信息
# # Django 默认可以使用任何 cache backend 作为 session backend, 将 django-redis 作为 session 储存后端不用安装任何额外的 backend
# # 将session的存储到Django缓存中
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"






