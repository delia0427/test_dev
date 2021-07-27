from django.db import models
from personal.models.project import Project


class Module(models.Model):
    """模块表"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # on_delete各参数的定义 删除关联关系，与之关联也删除
    name = models.CharField("名称", max_length=50, null=False)   # 名称：admin表新建的时候的显示名字
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态", default=1)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name