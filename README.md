# LittleServer

- Python 3.7.6 + Django3.1
- 安装项目依赖包requirements



### 项目结构

```
LittleServer
├── Dockerfile
├── FileSave                # FileSave app的实现
│   ├── Service
│   │   └── uploadSvc.py    # 上传文件服务
│   ├── models.py 
│   ├── static              # 放静态文件css，images等
│   ├── templates           # 放html文件
│   ├── urls.py             # 路由配置
│   ├── views.py            # 视图函数（业务逻辑）
│   └── ...
├── LittleServer            # 整个项目名
│   ├── asgi.py
│   ├── db.sqlite3  
│   ├── settings            # 项目的配置
│   │   ├── base.py         # 通用配置
│   │   ├── dev.py          # 开发环境的配置
│   │   └── prod.py         # 线上环境的配置
│   ├── urls.py             # 路由配置
│   └── wsgi.py
├── PasteBin                # PasteBin app的实现
│   ├── Service      
│   │   └── pasteSvc.py     # paste服务
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── static
│   ├── templates
│   ├── urls.py
│   ├── views.py
│   └── ...
├── README.md
├── TinyURL                   # TinyURL app的实现
│   ├── Service
│   │   ├── configSvc.py      # 域名拼接服务
│   │   ├── redisScv.py       # redis服务-存储 读取数据
│   │   └── tinyurlScv.py     # URL压缩服务
│   ├── apps.py    
│   ├── migrations
│   ├── models.py
│   ├── static
│   ├── templates
│   ├── urls.py
│   ├── views.py
│   └── ...
├── db.sqlite3
├── docker-compose.yml        # 通过docker-compose拉取容器的配置来源
├── manage.py
├── requirements.txt          # 项目依赖包
└── ...
```



### 主要功能

- 实现 TinyURL 功能
- 基于 Markdown 语法渲染以及 TinyURL 实现 PasteBin 功能
- 基于腾讯云对象存储服务（COS）实现 FileSave 功能
- 访问 [kiki.zone](https://www.kiki.zone.com) 即可



### 镜像构建

- 使用 GitHub Action 自动构建镜像，完成后自动发布到 Docker Hub 上



### 线上部署

- 在服务器上使用docker-compse配置部署





