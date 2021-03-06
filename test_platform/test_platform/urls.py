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
from django.contrib import admin
from django.urls import path, include
from personal.views import login_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', login_views.say_hello),
    path('index/', login_views.index),
    path('', login_views.index),  # 这样初始页面可以不用输入login
    path('logout/', login_views.logout),

    # project 管理
    path('project/', include('project_app.urls')),  # 项目管理

    # 模块管理
    path('module/', include('module_app.urls')),

    # 用例管理
    path('case/', include('case_app.urls')),

    # 任务管理
    path('task/', include('task_app.urls')),


]
