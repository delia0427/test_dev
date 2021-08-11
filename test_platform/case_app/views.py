from django.contrib.auth.decorators import login_required   # 需要登录可查看
from django.shortcuts import render  # 返回页面
from django.http import HttpResponse, JsonResponse  # 重定向
import requests
import json


@login_required()
def case_manage(request):
    """用例管理页"""
    return render(request, "case.html")


# @login_required()
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
                r = request.get(url, params=payload)
                print("jieguo:", r.json)
            else:
                r = request.get(url, params=payload, headers=header)
        if method == "post":
            if type_ == "form":
                if header == "":
                    r = request.post(url, data=payload)
                    print(r.text)
                else:
                    r = request.post(url, data=payload, headers=header)
                    print(r.text)
            if type_ == "json":
                if header == "":
                    r = request.post(url, json=payload)
                    print(r.text)
                else:
                    r = request.post(url, json=payload, headers=header)
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
        if assert_type == "contains":
            if assert_text not in result_text:
                return JsonResponse({"result": "断言失败"})
            else:
                return JsonResponse({"result": "断言成功"})
        if assert_type == "equals":
            if assert_text == result_text:
                return JsonResponse({"result": "断言成功"})
            else:
                return JsonResponse({"result": "断言失败"})     
    else:
        return JsonResponse({"result": "请求方法错误"})

