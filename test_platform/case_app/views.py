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
def case_manage(request):
    """用例管理页"""
    case_list = Case.objects.all()
    return render(request, "case_list.html", {"cases": case_list})


@login_required()
def case_debug(request):
    """测试用调试"""
    if request.method == "POST":
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        headers = request.POST.get("header", "")
        type_ = request.POST.get("type", "")
        parameter = request.POST.get("parameter", "")
        par_temp = parameter.replace("\'", "\"")
        try:
            payload = json.loads(par_temp)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数类型错误"})
        header_temp = headers.replace("\'", "\"")
        try:
            header = json.loads(header_temp)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "头类型错误"})
        if method == "get":
            if header == "":
                r = requests.get(url, params=payload)
                print("jieguo:", r.json)
            else:
                r = requests.get(url, params=payload, headers=header)
        if method == "post":
            if type_ == "form-data":
                if header == "":
                    r = requests.post(url, data=payload)
                    print(r.text)
                else:
                    r = requests.post(url, data=payload, headers=header)
                    print(r.text)
            if type_ == "JSON":
                if header == "":
                    r = requests.post(url, json=payload)
                    print(r.text)
                else:
                    r = requests.post(url, json=payload, headers=header)
                    print(r.text)
            print("jieguo:", r.json)
        return JsonResponse({"result": r.text})
    else:
        return JsonResponse({"result": "请求方法错误"})


@login_required()
def case_assert(request):
    """测试用例的断言"""
    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")
        assert_type = request.POST.get("assert_type", "")
        if result_text == "" or assert_text == "":
            return JsonResponse({"result": "断言文本不能为空"})
        if assert_type == "contain":
            if assert_text not in result_text:
                return JsonResponse({"result": "断言失败"})
            else:
                return JsonResponse({"result": "断言成功"})
        if assert_type == "equal":
            if assert_text == result_text:
                return JsonResponse({"result": "断言成功"})
            else:
                return JsonResponse({"result": "断言失败"})     
    else:
        return JsonResponse({"result": "请求方法错误"})


@login_required()
def case_save(request):
    """测试用例的保存"""
    if request.method == "POST":
        url = request.POST.get("url", "")
        method_t = request.POST.get("req_method", "")
        header = request.POST.get("header", "")
        module = request.POST.get("module_id", "")
        parameter_t = request.POST.get("par_type", "")
        parameter_body = request.POST.get("parameter", "")
        result_body = request.POST.get("result_text", "")
        assert_t = request.POST.get("assert_type", "")
        assert_text = request.POST.get("assert_result", "")
        name = request.POST.get("case_name", "")
        cid = request.POST.get("cid", "")
        if method_t == "get":
            method = 1
        else:
            method = 2
        if parameter_t == "form-data":
            parameter_type = 1
        else:
            parameter_type = 2
        if assert_t == "contain":
            assert_type = 1
        else:
            assert_type = 2
        if cid == "":
            Case.objects.create(name=name, module_id=int(module), header=header, url=url,
            method=method, parameter_body=parameter_body, parameter_type=parameter_type,result_body=result_body,
            assert_type=assert_type, assert_text=assert_text )
            return JsonResponse({"status": 10200, "message": "创建成功"})   # 可以改成重定向到case列表页
        else:
            case = Case.objects.get(id=cid)
            case.name = name
            case.module_id = int(module)
            case.header = header
            case.url = url
            case.method = method
            case.parameter_body = parameter_body
            case.parameter_type = parameter_type
            case.result_body = result_body
            case.assert_type = assert_type
            case.assert_text = assert_text
            case.save()
            return JsonResponse({"status": 10100, "message": "保存成功"})   # 可以改成重定向到case列表页
    else:
            return JsonResponse({"status": 10101, "message": "请求方法错误"})


@login_required()
def add_case(request):
    """测试用例的添加"""
    return render(request, "case_add.html")


@login_required()
def edit_case(request, cid):
    """测试用例的编辑"""
    return render(request, "case_edit.html", {"cid": cid})

@login_required()
def delete_case(request, cid):
    """测试用例的删除"""
    if request.method == "GET":
        try:
            case = Case.objects.get(id=cid)
        except Case.DoesNotExist:
            return HttpResponseRedirect("/case/")
        else:
            case.delete()
        return HttpResponseRedirect("/case/")
    else:
        return HttpResponseRedirect("/case/")


@login_required()
def get_case_info(request):
    """获取接口数据"""
    if request.method == "POST":
        cid = request.POST.get("cid", "")
        case = Case.objects.get(id=cid)
        module = Module.objects.get(id=case.module_id)
        if case.method == 1:
            method = "get"
        else:
            method = "post"
        if case.parameter_type == 1:
            parameter_type = "form-data"
        else:
            parameter_type = "JSON"
        if case.assert_type == 1:
            assert_type = "contain"
        else:
            assert_type = "equal"


        case_dict = {
            "id": case.id,
            "url": case.url,
            "name": case.name,
            "method": method,
            "header": case.header,
            "parameter_type": parameter_type,
            "parameter_body": case.parameter_body,
            "result_body": case.result_body,
            "aesert_type": assert_type,
            "assert_text": case.assert_text,
            "module_id": case.module_id,
            "project_id": module.project_id

        }
        return JsonResponse({"status:10200,"
                             "message": "请求成功",
                             "result": case_dict})
    else:
        return JsonResponse({"result": "请求方法错误"})


@login_required()
def get_select_data(request):
    """获取项目>模块列表"""
    if request.method == "GET":
        projects = Project.objects.all()
        project_list = []
        for project in projects:
            project_dict = {
                "id": project.id,
                "name": project.name
            }
            modules = Module.objects.filter(project_id=project.id)
            module_list = []
            for module in modules:
                module_list.append({
                    "id": module.id,
                    "name": module.name
                })
            project_dict["module_list"] = module_list
            project_list.append(project_dict)
        return JsonResponse({"status": 10200, "message": "success", "data": project_list})
    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})

