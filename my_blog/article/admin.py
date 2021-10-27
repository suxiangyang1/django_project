from django.contrib import admin
# 导入ArticlePost
from .models import ArticlePost


# 注册ArticlePost 到admin 中
admin.site.register(ArticlePost)
