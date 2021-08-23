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
from module_app import views


urlpatterns = [

    path('', views.module_manage),  # 模块管理
    path('add_module/', views.add_module),  # 添加项目页面
    path('edit_module/<int:mid>/', views.edit_module),  # 编辑项目页面
    path('delete_module/<int:mid>/', views.delete_module),  # 添加项目页面

    # 接口
    path('module_list', views.module_list),  # 根据项目id查看模块列表




]
