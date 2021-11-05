from django.shortcuts import render, redirect
# 导入HttpResponse 模块
from django.http import HttpResponse
from .models import ArticlePost
# 引入刚才的ArticlePostForm表单类
from .forms import ArticlePostForm
# 引入markdown模块
import markdown
# 引入刚定义的ArticlePostForm 表单类
from .forms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User


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


# 写文章的视图
def article_create(request):
    # 判断用户是否提交数据
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的额要求
        if article_post_form.is_valid():
            # 保存数据, 但暂时不提交到数据中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果进行过删除数据表的操作, 可能会找不到id=1的用户
            # 此时请重新创建用户, 并传入此用户的id
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据中
            new_article.save()
            # 完成后返回到文章列表中
            return redirect("article:article_list")
        # 如果数据不合法, 返回错误信息
        else:
            return HttpResponse("表单内容有误， 请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = { 'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'article/create.html', context)


# 删除文章
def article_delete(request, id):
    # 根据id 获取需要删除的文章
    article = ArticlePost.objects.get(id=id)
    # 调用 .delete 方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("article:article_list")


# 安全删除文章
def article_safe_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse('仅允许post请求')


## 更新文章
def article_update(request, id):
    """
    更新文章的视图函数
    通过POST方法提交表单, 更新title 、 body 字段
    GET 方法进入初始表单页面
    :param request:
    :param id:  文章的id
    :return:
    """

    # 获取需要修改的具体文章对象
    article = ArticlePost.objects.get(id=id)
    # 判断用户是否为POST 提交表单数据
    if request.method == 'POST':
        # 将提交到数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            # 完成后返回到修改的文章中。 需要传入文章的id 值
            return redirect("article:article_detail", id=id)
        # 如果数据不合法 返回错误休息
        else:
            return HttpResponse("表达那有误, 请重新填写。")
    # 如果用户 GET 请求数据
    else:
        # 创建表单实例
        article_post_form = ArticlePostForm()
        # 赋值上下文, 将article 文章对象也传递进去 以便提取旧的内容
        context = { 'article': article, 'article_post_form': article_post_form }
        # 将响应返回到模板中
        return render(request, 'article/update.html', context)




