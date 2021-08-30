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


def get_case_tree(request):
    """获取case的tree"""
    if request.method == "GET":
        project_list = Project.objects.all()
        data_list = []
        for project in project_list:
            dict_temp = {"id": project.id, "pId": 0, "name": project.name, "open": False}
            data_list.append(dict_temp)
            module_list = Module.objects.filter(project=project.id)
            if module_list:
                for module in module_list:
                    dict_temp = {"id": module.id+10000, "pId": project.id, "name": module.name, "open": False}
                    data_list.append(dict_temp)
                    case_list = Case.objects.filter(module=module.id)
                    if case_list:
                        for case in case_list:
                            dict_temp = {"id": case.id+100, "pId": module.id+10000, "name": case.name, "open": False}
                            data_list.append(dict_temp)
        return JsonResponse({"status": 10200, "message": "success", "data": data_list})
    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})