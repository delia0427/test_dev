from django.http import HttpResponse, HttpResponseRedirect  # 重定向
from django.shortcuts import render  # 返回页面
from django.contrib import auth
from django.contrib.auth.decorators import login_required   # 需要登录可查看


def say_hello(request):
    name = request.GET.get("name","")
    if name == "":
        return HttpResponse("请输入name")
    # html = "<h1>hello," + name +"</h1><br>"  # 直接返回html信息
    return render(request, "index.html", {"name": name})  # 返回对应页面 ，可以传参

def index(request):
    """登录"""
    # 获取前端输入
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
    if username == "" or password == "":
        return render(request, "index.html",{
            "error": "用户名或密码为空"
        })
    # 使用auth判断
    user = auth.authenticate(username=username, password=password)
    # 判断错误，返回错误信息
    if user is None:
        return render(request, "index.html", {
            "error":"yyonghum huo mima 错误"
        })
    # 判断正确，跳转
    else:
        auth.login(request, user)  # 记录用户的登录状态
        # render(request, "project.html")
        return HttpResponseRedirect("/project/")  # 重定向到manage页面


def logout(request):
    """处理用户退出"""
    auth.logout(request)  # 自动清除session表里的sessionId
    return HttpResponseRedirect("/index/")  # 重定向到登录页


@login_required()
def project_manage(request):
    """登录成功，默认项目管理页"""
    return render(request, "project.html")


@login_required()
def module_manage(request):
    """模块管理页面"""
    return render(request, "module.html")

#
# @register.filter
# def my_filter(v1, v2):
#     return v1 * v2
#
#
# @register.simple_tag
# def my_tag1(v1, v2, v3):
#     return v1 * v2 * v3



