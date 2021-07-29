from django.contrib.auth.decorators import login_required   # 需要登录可查看
from personal.models.project import Project
from django.shortcuts import render  # 返回页面


@login_required()
def project_manage(request):
    """登录成功，默认项目管理页"""
    project_all = Project.objects.all()  # 读取数据库peojects所有数据，传给html
    return render(request, "project.html", {"projects": project_all,
                                            "type":"list"})

@login_required()
def add_project(request):
    """添加项目"""
    # project_all = Project.objects.all()  # 读取数据库peojects所有数据，传给html
    return render(request, "project.html", {"type":"add"})