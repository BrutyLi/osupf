from django.db import models

# Create your models here.


class hostInfo(models.Model):
    hname=models.CharField(max_length=32,verbose_name='描述',blank=True)
    hip=models.GenericIPAddressField(verbose_name='IPadd')
    hcpu=models.CharField(max_length=8,verbose_name='cpu',)
    hdisk=models.CharField(max_length=16,verbose_name='磁盘')
    huser=models.CharField(max_length=128,verbose_name='用户信息')
    hlog=models.TextField(max_length=10240,verbose_name='日志')

    def __str__(self):
        return self.hname

    class Meta:
        verbose_name='主机信息'
        verbose_name_plural='主机信息'
