from django.db import models
from case_app.models import Case


class Task(models.Model):
    """任务表"""
    name = models.CharField("名称", max_length=50, null=False)   # 名称：admin表新建的时候的显示名字
    desc = models.TextField("描述", null=False)   # 1：GET 2：POST 3：DELETE 4：PUT
    cases = models.TextField("用例", null=False)
    status = models.IntegerField("请求方法", default=0)   # 1：已执行 2：未执行
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name
