from django.shortcuts import render
# 导入HttpResponse 模块
from django.http import HttpResponse
from .models import ArticlePost
# 引入markdown模块
import markdown


# 视图函数
def article_list(request):
    # return HttpResponse("Hello, World")
    # 改写视图函数
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板 (templates) 的对象
    context = {'articles': articles}
    # render 函数: 载入模板 并且返回context对象
    return render(request, 'article/list.html', context)

"""
解释:
    ArticlePost.objects.all() ------>  可获得所有的对象(即博客文章
    context    ----->    定义了需要传递给模板的上下文, 这里即 articles
    render函数  ----->    结合模板上下文, 并返回渲染后的HttpResponse对象, 即把
context内容添加进模板, 通过浏览器实现
   
   render 变量分解如下:
        request是固定的request对象, 照写就行
        article/list.html    定义了模板文件的上下文
        context 定义了需要传入模板文件的上下文 
"""


# 文章详情(引用markdown来对详情页进行改写)
def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)

    # 将markdown 语法渲染成html样式
    # markdown.markdown语法接收两个参数: 第一个参数是: 需要渲染的正文 ; 第二个参数载入了常用的语法扩展。
    article.body = markdown.markdown(article.body,
        extensions=[
            # 包含 缩写 表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮
            'markdown.extensions.codehilite',
        ])

    # 需要传递给模板的对象
    context = {'article': article}
    # 载入模板, 并返回context对象
    return render(request, 'article/detail.html', context)

