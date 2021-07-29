from django.contrib.auth.decorators import login_required   # 需要登录可查看
from personal.models.project import Project
from django.shortcuts import render  # 返回页面


@login_required()
def module_manage(request):
    """模块管理页面"""
    return render(request, "module.html")