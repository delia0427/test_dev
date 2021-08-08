from django.contrib import admin
from module_app.models import Module
# Register your models here.


class ModuleAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "status", "create_time", "project"]
    list_filter = ["project"]  # 过滤栏


admin.site.register(Module, ModuleAdmin)  # 把自己建的表加入admin后台
