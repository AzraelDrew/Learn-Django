from django.conf import settings

import hashlib


def md5(data_string):
    """ md5加密 """
    # 随机数
    obj = hashlib.md5(settings.SECRET_KEY.encode("utf-8"))
    # 没有随机数的加密
    # obj = hashlib.md5()
    obj.update(data_string.encode("utf-8"))
    return obj.hexdigest()