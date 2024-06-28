# PaddleOCR-python-server
Course Reports-This repository will be removed in August


参考https://docs.djangoproject.com/zh-hans/4.0/安装好django，
使用django-admin startproject dlIntegrated创建一个项目
使用python manage.py runserver运行服务器，
浏览器输入localhost:8080可以访问网站则配置成功。
6.2创建app
使用python manage.py startapp paddleApp创建app
配置dlIntegrated/setting.py配置项，连接数据库，连接App等，找到 INSTALLED_APPS，加入app选项paddleApp.apps.PaddleappConfig(根据自己项目调整)
6.2.1 安装 PaddleOCR
GPU版本python3 -m pip install paddlepaddle-gpu要求配置好cuda环境，在app 中的 urls.py 中定义 url 接口，将app 中 API接口与项目链接。
