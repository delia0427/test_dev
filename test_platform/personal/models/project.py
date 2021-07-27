from django.db import models


class Project(models.Model):  # 相当于创建一张表
    """项目表"""
    name = models.CharField("名称", max_length=50, null=False)   # 名称：admin表新建的时候的显示名字
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态", default=1)
    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name



