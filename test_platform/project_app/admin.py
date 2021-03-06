from django.contrib import admin
from project_app.models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "status", "create_time"]
    search_fields = ["name"]   # 搜索栏
    list_filter = ["status"]  # 过滤栏


admin.site.register(Project, ProjectAdmin)  # 把自己建的表加入admin后台
