from django.contrib.auth.decorators import login_required   # 需要登录可查看
from django.shortcuts import render  # 返回页面
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect  # 重定向
import requests
import json
from case_app.models import Case
from module_app.models import Module
from project_app.models import Project
from task_app.models import Task
from django.core.paginator import  Paginator


@login_required()
def task_manage(request):
    """任务管理"""
    task_list = Task.objects.all()
    return render(request, "task_list.html", {"type": "list", "tasks": task_list})


@login_required()
def add_task(request):
    """创建任务"""
    return render(request, "task_add.html", {"type": "add"})


def save_task(request):
    """获取case的tree"""
    if request.method == "POST":
        name = request.POST.get("name", "")
        desc = request.POST.get("desc", "")
        cases = request.POST.get("cases", "")
        if name == "" or cases == "":
            return JsonResponse({"status": 10102, "message": "名称或用例参数不能为空"})
        Task.objects.create(name=name, desc=desc, cases=cases)
        return JsonResponse({"status": 10200, "message": "success"})
    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


def get_case_tree(request):
    """保存任务"""
    project_list = Project.objects.all()
    data_list = []
    for project in project_list:
        dict_temp = {"id": project.id+10000, "pId": 0, "name": project.name, "open": False, "isParent": True}
        data_list.append(dict_temp)
        module_list = Module.objects.filter(project=project.id)
        if module_list:
            for module in module_list:
                dict_temp = {"id": module.id+100, "pId":  project.id+10000, "name": module.name,
                             "open": False, "isParent": True}
                data_list.append(dict_temp)
                case_list = Case.objects.filter(module=module.id)
                if case_list:
                    for case in case_list:
                        dict_temp = {"id": case.id, "pId": module.id+100,
                                     "name": case.name, "open": False,
                                     "isParent": False}
                        data_list.append(dict_temp)
    if request.method == "GET":
        return JsonResponse({"status": 10200, "message": "success", "data": data_list})
    elif request.method == "POST":
        tid = request.POST.get("tid", "")
        if tid == "":
            return JsonResponse({"status": 10100, "message": "renwu id buneng weikong!"})
        task = Task.objects.get(id=tid)
        caseList = json.loads(task.cases)  # 将数据库中字符串转化成list
        task_data = { "name": task.name, "desc": task.desc}
        # 处理数据

        task_data["data"] = data_list
        return JsonResponse({"status": 10200, "message": "success", "data": task_data})


@login_required()
def edit_task(request, tid):
    """测试任务的编辑"""
    return render(request, "task_edit.html", {"type": "edit"})


@login_required()
def delete_task(request, tid):
    """测试用例的删除"""
    if request.method == "GET":
        try:
            task = Task.objects.get(id=tid)
        except task.DoesNotExist:
            return HttpResponseRedirect("/task/")
        else:
            task.delete()
        return HttpResponseRedirect("/task/")
    else:
        return HttpResponseRedirect("/task/")

