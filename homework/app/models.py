from django.db import models

# Create your models here.
# 部门表
class Department(models.Model):
    title = models.CharField(verbose_name="标题",max_length=32)   # verbose_name  对当前列进行备注(可以写可不写)

    def __str__(self) :
        return self.title

# 员工表
class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    age  = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    # max_digits=10        最多多少位
    # decimal_places=2     小数点后多少位
    create_time = models.DateTimeField(verbose_name="入职时间")

    # 无约束
    # depart_id = models.BigIntegerField(verbose_name="部门ID")

    # 有约束
    # to  表示与那张表又关联
    # to_fied   关联表中的那一列
    # on_delete=models.CASCADE   级联删除  当部门被删除时用户也被删除
    depart = models.ForeignKey(verbose_name="部门",to="Department", to_field="id", on_delete=models.CASCADE)
    # 置为空null=True,blank=True ,on_delete=models.SET_NULL
    # depart = models.BigIntegerField(verbose_name="部门ID",to="Department", to_field="id",null=True,blank=True ,on_delete=models.SET_NULL)

    # 在Django中约束   choices=gender_choices
    gender_choices =(
        (1,"男"),
        (2,"女")
    )
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices)