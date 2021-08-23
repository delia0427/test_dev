from django.contrib.auth.decorators import login_required   # 需要登录可查看
from django.shortcuts import render  # 返回页面
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect  # 重定向
import requests
import json
from case_app.models import Case
from module_app.models import Module
from project_app.models import Project
from django.core.paginator import  Paginator


@login_required()
def task_manage(request):
    """任务管理"""
    return render(request, "task_list.html", {"type": "list"})


@login_required()
def add_task(request):
    """创建任务"""
    return render(request, "task_add.html", {"type": "add"})
