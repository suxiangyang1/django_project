from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import UserloginForm

#引入logout 模块
from django.contrib.auth import authenticate, login , logout
# 引入 UserRegisterForm 表单类
from .forms import UserloginForm, UserRegisterForm
# Create your views here.


# 用户登录
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserloginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配返回这个 user 对象
            # authenticate  ----->   验证用户名和密码是否匹配
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在session 中 即实现了登录动作
                # Session在网络应用中，称为**“会话控制”**，它存储特定用户会话所需的属性及配置信息
                login(request, user)
                return redirect('article:article_list')
            else:
                return HttpResponse("账号密码输入错误, 请重新输入~")
        else:
            return HttpResponse("账号或密码不合法~")
    elif request.method == 'GET':
        user_login_form = UserloginForm()
        context = { 'form': user_login_form }
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("请使用GET或者POST请求数据！")


# 用户退出
def user_logout(request):
    logout(request)
    return redirect("article:article_list")


# 用户注册
def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存好数据后立即登录并返回博客列表页面
            login(request, new_user)
            return redirect("article:article_list")
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")



