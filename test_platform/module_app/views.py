from django.contrib.auth.decorators import login_required  # 需要登录可查看
from django.shortcuts import render  # 返回页面
from module_app.models import Module
from module_app.forms import ModuleForm
from django.http import HttpResponseRedirect, JsonResponse  # 重定向


@login_required()
def module_manage(request):
    """模块管理页面"""
    module_all = Module.objects.all()  # 读取数据库peojects所有数据，传给html
    # print(module_all.get(id=1))
    return render(request, "module.html", {"modules": module_all,
                                           "type": "list"})


@login_required()
def add_module(request):
    """添加模块"""
    if request.method == "GET":
        module_form = ModuleForm()
        return render(request, "module.html", {"form": module_form, "type": "add"})
    elif request.method == "POST":
        name = request.POST.get("name", "")
        describe = request.POST.get("describe", "")
        status = request.POST.get("status", "")
        project = request.POST.get("project", "")
        print(status)
        if name == "":
            return render(request, "module.html", {"type": "add",
                                                   "name_error": "项目名字不能为空"})
        Module.objects.create(name=name, describe=describe, status=status, project_id=project)
    return HttpResponseRedirect("/module/")


@login_required()
def edit_module(request, mid):
    """编辑模块"""
    if request.method == "GET":
        if mid:
            p = Module.objects.get(id=mid)
            form = ModuleForm(instance=p)  # 表单默认值
            return render(request, "module.html", {"type": "edit",
                                                   "form": form,
                                                   "mid": mid})
    elif request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]
            status = form.cleaned_data["status"]
            project = form.cleaned_data["project"]
            p = Module.objects.get(id=mid)
            p.name = name
            p.describe = describe
            p.status = status
            p.project = project
            p.save()
        return HttpResponseRedirect("/module/")


@login_required()
def delete_module(request, mid):
    """删除模块"""
    if request.method == "GET":
        try:
            module = Module.objects.get(id=mid)
        except Module.DoesNotExist:
            return HttpResponseRedirect("/module/")
        else:
            module.delete()
        return HttpResponseRedirect("/module/")
    else:
        return HttpResponseRedirect("/module/")


def module_list(request):
    """
    接口：根据项目id，返回对应的模块列表
    """
    if request.method == "POST":
        pid = request.POST.get("pid", "")
        if pid == "":
            return JsonResponse({"status":10102,"message": "项目id不能为空"})
        modules = Module.objects.filter(project=pid)
        modules_list = []
        for mod in modules:
            module_dict = {
                "id":  mod.id,
                "name": mod.name
            }
            modules_list.append(module_dict)
        return JsonResponse({"status": 10200, "message": "请求成功", "data": modules_list})
    else:
        return JsonResponse({"status": 10101, "message": "请求方法错误"})
