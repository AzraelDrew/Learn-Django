from django import forms


class BootStrapModelForm(forms.ModelForm):
    """ ModelFormBootStrap样式 """
    bootstrap_exclude_fields = ['img']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, item in self.fields.items():
            # 此方法会将原有的属性覆盖
            # item.widget.attrs = {"class":"form-control","placeholder":item.label}

            # 保留原来都属性,若没有属性则添加属性
            if name in self.bootstrap_exclude_fields:
                continue
            if item.widget.attrs:
                item.widget.attrs["class"] = "form-control"
                item.widget.attrs["placeholder"] = item.label
            else:
                item.widget.attrs = {
                    "class": "form-control",
                    "placeholder": item.label
                }


class BootStrapForm(forms.Form):
    """ FormBootStrap样式 """
    # 需要忽略样式的字段
    bootstrap_exclude_fields = ['img']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, item in self.fields.items():
            # 此方法会将原有的属性覆盖
            # item.widget.attrs = {"class":"form-control","placeholder":item.label}

            # 保留原来都属性,若没有属性则添加属性

            if name in self.bootstrap_exclude_fields:
                continue

            if item.widget.attrs:
                item.widget.attrs["class"] = "form-control"
                item.widget.attrs["placeholder"] = item.label
            else:
                item.widget.attrs = {
                    "class": "form-control",
                    "placeholder": item.label
                }
