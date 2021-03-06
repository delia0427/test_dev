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
from task_app import views


urlpatterns = [

    path('', views.task_manage),  # 任务管理
    path('add_task/', views.add_task),  # 增加任务
    path('save_task', views.save_task),  # 保存任务
    path('edit_task/<int:tid>/', views.edit_task),
    path('delete_task/<int:tid>/', views.delete_task),
    path('get_case_tree', views.get_case_tree)   # 获取项目模块用例的树形结构






]
