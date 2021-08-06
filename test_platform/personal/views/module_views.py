from django.contrib.auth.decorators import login_required   # 需要登录可查看
from personal.models.module import Module
from django.shortcuts import render  # 返回页面


@login_required()
def module_manage(request):
    """模块管理页面"""
    return render(request, "module.html")


@login_required()
def add_module(request):
    """添加模块"""
    pass


@login_required()
def edit_module(request, mid):
    """编辑模块"""
    if request.method == "GET":
        module = Module.objects.get(id=mid)



@login_required()
def delete_module(request):
    """添加模块"""
    pass

