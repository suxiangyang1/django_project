# 引入path
from django.urls import path
from . import views

# 正在部署的应用的名称
# app的urls.py必须配置app_name，否则会报错
app_name = 'article'

urlpatterns = [
    # path函数将url 映射到视图
    path('article-list/', views.article_list, name='article_list'),

    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),

    # 写文章
    path('article-create/', views.article_create, name='article_create'),
]