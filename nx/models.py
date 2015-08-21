# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
from datetime import time
import re
from django.contrib import admin

from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.db import models


def get_upload_file_name(instance, filename):
    return "galleries/%s_%s" % (str(time()).replace('.', '_'), filename)


class Donate(models.Model):
    username = models.CharField("用户名", max_length=30)
    phone_number = models.CharField("手机号", max_length=11,
                                    validators=[
                                        validators.RegexValidator(re.compile('^\+?1?\d{9,15}$'),
                                                                  _('请输入有效的电话号码'), 'invalid')
                                    ])

    address = models.CharField("地址", max_length=100)
    donation_type = models.CharField("类型", max_length=10)
    new = models.BooleanField("新", default=False, help_text="捐赠物品是不是新的")
    number = models.IntegerField("数量", max_length=10)
    photo = models.ImageField(upload_to=get_upload_file_name,
                              help_text="选择图片")
    description = models.TextField("简介")
    timestamp = models.DateTimeField(auto_now=True)
    validate = models.BooleanField("是否验证", default=False)
    status = models.BooleanField("是否已经发送", default=False)
    type = models.CharField("类型", max_length=10, default='note')

    def __unicode__(self):
        return self.username

    def get_photo_url(self):
        return self.photo.url

class Need(models.Model):
    publisher = models.CharField("发布者", max_length=30)
    publisher_phone_number = models.CharField("手机号", max_length=11,
                                    validators=[
                                        validators.RegexValidator(re.compile('^\+?1?\d{9,15}$'),
                                                                  _('请输入有效的电话号码'), 'invalid')
                                    ])

    image = models.ImageField(upload_to=get_upload_file_name,
                              help_text="选择图片")
    address = models.CharField("地址", max_length=20)
    contact_person = models.CharField("联系人", max_length=11)
    contact_person_telephone = models.CharField("联系人手机号", max_length=11,
                                    validators=[
                                        validators.RegexValidator(re.compile('^\+?1?\d{9,15}$'),
                                                                  _('请输入有效的电话号码'), 'invalid')
                                    ])
    description = models.TextField("简介")
    type = models.CharField("类型", max_length=10, default='need')
    def __unicode__(self):
        return self.publisher

    def get_image_url(self):
        return self.image.url

admin.site.register(Need)
admin.site.register(Donate)
