# Django
> 项目结构
- db.sqlite3    一个轻量级的数据库文件, 用来存储项目产生的数据, 比如博客文章; manage.py是项目执行命令的窗口，比如runserver
- app      用来放置博客文章的相关代码; 后台管理文件admin.py, 数据模型文件models.py, 视图文件views.py，
存放签约文件的目录migrations.
- settings.py 包含项目的配置参数
- urls.py 则是项目的根路由文件

### 注册APP (settings)
```
my_blog/settiings.py

INSTALLED_APPS = [
    # 其他代码
    ...
    
    # 激活新增的app(例如)
    'article',
    
]
```

### 配置访问路径 (urls)
> 给app配置访问路径url, 配置好url后Django 才知道如何定位app.

打开my_blog 目录下的urls.py ,增加如下代码
```text
my_blog/urls.py

from django.contrib import admin
# 记得引入include
from django.urls import path, include

# 存放映射关系的列表
urlpatterns = [
    path('admin/', admin.site.urls),

    # 新增代码，配置app的url
    path('article/', include('article.urls', namespace='article')),
]
```

### 框架
##### Django 框架主要关注的是模型(Model)、模板(Template) 和 视图(Views), 称为MTV模式。
- model ---->  数据存取层
- Template  -----> 业务逻辑层
- View  ------>    表现层

总结: Model存取数据, View决定需要调取哪些数据, 而Template则负责将调取出的数据以合理的方式展现出来。























