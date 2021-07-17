from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    name = request.GET.get("name","")
    if name == "":
        return HttpResponse("请输入name")
    # html = "<h1>hello," + name +"</h1><br>"  # 直接返回html信息
    return render(request, "index.html", {"name": name})  # 返回对应页面 ，可以传参

