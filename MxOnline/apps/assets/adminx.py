# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 23:52
# @Author  : 暖先生！
# @FileName: adminx.py
# @Software: PyCharm
# @Blog    ：http://www.zstcl.com
import xadmin
from .models import Equipment


class EquipmentAdmin(object):
    list_display = ['hostname', 'ip', 'information', 'OSname', 'role', 'buildtime', 'service', 'manager', 'area', 'beizhu']
    search_fields = ['hostname', 'ip', 'information', 'OSname', 'role', 'service', 'manager', 'area', 'beizhu']
    list_filter = ['hostname', 'ip', 'information', 'OSname', 'role', 'buildtime', 'service', 'manager', 'area', 'beizhu']


xadmin.site.register(Equipment, EquipmentAdmin)