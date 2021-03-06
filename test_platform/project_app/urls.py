"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from project_app import views


urlpatterns = [

    # 项目 管理
    path('', views.project_manage),  # 项目管理
    path('add_project/', views.add_project),  # 添加项目页面
    path('edit_project/<int:pid>/', views.edit_project),  # 编辑项目页面
    path('delete_project/<int:pid>/', views.delete_project),  # 添加项目页面

    # 接口实现—
    path('project_list', views.project_list),  # 查看项目列表


]
