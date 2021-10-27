from django.shortcuts import render
# 导入HttpResponse 模块
from django.http import HttpResponse
from .models import ArticlePost


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

