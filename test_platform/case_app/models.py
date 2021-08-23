from django.db import models
from module_app.models import Module


class Case(models.Model):
    """用例表"""
    module = models.ForeignKey(Module, on_delete=models.CASCADE)  # on_delete各参数的定义 删除关联关系，与之关联也删除
    name = models.CharField("名称", max_length=50, null=False)   # 名称：admin表新建的时候的显示名字
    url = models.TextField("URL", null=False)   # 1：GET 2：POST 3：DELETE 4：PUT
    method = models.IntegerField("请求方法", null=True)   # CharField 一定要定义对打长度，TextField不需要
    header = models.TextField("请求头", null=True)   #
    parameter_type = models.IntegerField("参数类型", null=True)   # 1：form-data 2：JSON
    parameter_body = models.TextField("参数内容", null=True)   #
    result_body = models.TextField("结果", null=True)   #
    assert_type = models.IntegerField("断言类型", null=True)   # 1：contain 2：equal
    assert_text = models.TextField("断言", null=True)   #
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name
