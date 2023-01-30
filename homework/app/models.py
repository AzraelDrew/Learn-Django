from django.db import models

# Create your models here.


# 管理员
class Admin(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    # 设置关联当前表时的返回值    若不设置返回值则 默认是一个对象
    def __str__(self):
        return self.username
        # return


# 部门表
class Department(models.Model):
    title = models.CharField(verbose_name="标题",
                             max_length=32)  # verbose_name  对当前列进行备注(可以写可不写)

    def __str__(self):
        return self.title


# 员工表
class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额",
                                  max_digits=10,
                                  decimal_places=2,
                                  default=0)
    # max_digits=10        最多多少位
    # decimal_places=2     小数点后多少位

    # create_time = models.DateTimeField(verbose_name="入职时间")

    #  DateTimeField  包括时分秒
    create_time = models.DateField(verbose_name="入职时间")

    # DateField  不包括时分秒

    # 无约束
    # depart_id = models.BigIntegerField(verbose_name="部门ID")

    # 有约束
    # to  表示与那张表又关联
    # to_fied   关联表中的那一列
    # on_delete=models.CASCADE   级联删除  当部门被删除时用户也被删除
    depart = models.ForeignKey(verbose_name="部门",
                               to="Department",
                               to_field="id",
                               on_delete=models.CASCADE)
    # 置为空null=True,blank=True ,on_delete=models.SET_NULL
    # depart = models.BigIntegerField(verbose_name="部门ID",to="Department", to_field="id",null=True,blank=True ,on_delete=models.SET_NULL)

    # 在Django中约束   choices=gender_choices
    gender_choices = ((1, "男"), (2, "女"))
    gender = models.SmallIntegerField(verbose_name="性别",
                                      choices=gender_choices)


# 靓号
class PrettyNumber(models.Model):
    mobile = models.CharField(verbose_name="手机号", max_length=32)
    price = models.IntegerField(verbose_name="价格", default=0)
    level_choices = (
        (1, "一星"),
        (2, "二星"),
        (3, "三星"),
        (4, "四星"),
        (5, "五星"),
    )
    level = models.SmallIntegerField(verbose_name="级别",
                                     choices=level_choices,
                                     default=1)

    status_choices = (
        (1, "已占用"),
        (2, "未占用"),
    )
    status = models.SmallIntegerField(verbose_name="状态",
                                      choices=status_choices,
                                      default=1)


# 任务
class Task(models.Model):
    level_choices = ((1, "紧急"), (2, "重要"), (3, "临时"))
    level = models.SmallIntegerField(verbose_name="级别",
                                     choices=level_choices,
                                     default=1)
    user = models.ForeignKey(verbose_name="负责人",
                             to="Admin",
                             on_delete=models.CASCADE)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")


class Order(models.Model):
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=64)
    price = models.IntegerField(verbose_name="价格")

    status_choices = ((1, "待支付"), (2, "已支付"))
    status = models.SmallIntegerField(verbose_name="状态",
                                      choices=status_choices,
                                      default=1)

    admin = models.ForeignKey(verbose_name="管理员",
                              to="Admin",
                              on_delete=models.CASCADE)


# from上传
class Boos(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    img = models.CharField(verbose_name="头像", max_length=128)


#  modelform上传
class City(models.Model):
    name = models.CharField(verbose_name="名称", max_length=32)
    count = models.IntegerField(verbose_name="人口")
    # 本质上号数据库存储的也是CharField,   优点是自动保存数据
    img = models.FileField(verbose_name="Logo",
                           max_length=128,
                           upload_to='city/')  # upload_to  为media的那个目录
