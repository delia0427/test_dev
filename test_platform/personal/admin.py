from django.contrib import admin
from personal.models.project import Project
from personal.models.module import Module


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "status", "create_time"]
    search_fields = ["name"]   # 搜索栏
    list_filter = ["status"]  # 过滤栏


class ModuleAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "status", "create_time", "project"]
    list_filter = ["project"]  # 过滤栏


admin.site.register(Project, ProjectAdmin)  # 把自己建的表加入admin后台
admin.site.register(Module, ModuleAdmin)  # 把自己建的表加入admin后台

