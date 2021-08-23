from django.contrib.auth.decorators import login_required   # 需要登录可查看
from project_app.models import Project
from django.shortcuts import render  # 返回页面
from project_app.forms import ProjectForm
from django.http import HttpResponseRedirect,JsonResponse  # 重定向



@login_required()
def project_manage(request):
    """登录成功，默认项目管理页"""
    project_all = Project.objects.all()  # 读取数据库peojects所有数据，传给html
    return render(request, "project.html", {"projects": project_all,
                                            "type": "list"})


@login_required()
def add_project(request):
    """添加项目"""
    if request.method == "GET":
        return render(request, "project.html", {"type": "add"})
    elif request.method == "POST":
        name = request.POST.get("name", "")
        describe = request.POST.get("describe", "")
        status = request.POST.get("status", "")
        if name == "":
            return render(request, "project.html", {"type": "add",
                                                    "name_error": "项目名字不能为空"})
        Project.objects.create(name=name, describe=describe, status=status)
    return HttpResponseRedirect("/project/")


@login_required()
def edit_project(request, pid):
    """编辑项目"""
    if request.method == "GET":
        if pid:
            p = Project.objects.get(id=pid)
            form = ProjectForm(instance=p)  # 表单默认值
            return render(request, "project.html", {"type": "edit",
                                                    "form": form,
                                                    "pid": pid})
    elif request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]
            status = form.cleaned_data["status"]
            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()
        return HttpResponseRedirect("/project/")



@login_required()
def delete_project(request, pid):
    """删除项目"""
    if request.method == "GET":
        try:
            project = Project.objects.get(id=pid)
        except Project.DoesNotExist:
            return HttpResponseRedirect("/project/")
        else:
            project.delete()
        return HttpResponseRedirect("/project/")
    else:
        return HttpResponseRedirect("/project/")


def project_list(request):
    """
    接口：获取项目列表
    """
    if request.method == "GET":
        projects = Project.objects.all()
        projects_list = []
        for pro in projects:
            projetc_dict = {
                "id":  pro.id,
                "name": pro.name
            }
            projects_list.append(projetc_dict)
        return JsonResponse({"status": 10200, "message": "请求成功", "data": projects_list})

    else:
        return JsonResponse({"status": 10101, "message": "请求方法错误"})
