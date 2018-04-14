# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Equipment(models.Model):
    hostname = models.CharField(max_length=50, verbose_name=u"主机名", default="")
    ip = models.CharField(max_length=50, verbose_name=u"IP地址", default="")
    information = models.CharField(max_length=300, verbose_name=u"硬件配置", default="")
    OSname = models.CharField(max_length=300, verbose_name=u"系统镜像", default="")
    role = models.CharField(max_length=50, choices=(("Product", u"生产环境"), ("Test", u"测试环境")), default="Test",verbose_name=u"所属环境")
    buildtime = models.DateField(verbose_name=u"创建时间", null=True, blank=True)
    service = models.CharField(max_length=600, default="", verbose_name=u"部署服务")
    manager = models.CharField(max_length=300, default="", verbose_name=u"负责人")
    area = models.CharField(max_length=50, default="", verbose_name=u"地区")
    beizhu = models.CharField(max_length=300, default="", verbose_name=u"备注")


    class Meta:
        verbose_name = "资产信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}'.format(self.hostname)
