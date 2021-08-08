from django import forms
from module_app.models import Module


class ModuleForm(forms.ModelForm):
    # name = forms.CharField(label="名称", max_length=100)
    # describe = forms.CharField(label="描述", widget=forms.Textarea)
    # status = forms.BooleanField(label="状态", required=True)
    class Meta:
        model = Module
        fields = ["id", "name", "describe", "status", "project"]
