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


class Note(models.Model):
    username = models.CharField("用户名", max_length=30)
    phone_number = models.CharField("手机号", max_length=11,
                                    validators=[
                                        validators.RegexValidator(re.compile('^\+?1?\d{9,15}$'),
                                                                  _('Enter a valid Phone Number.'), 'invalid')
                                    ])

    address = models.CharField("地址", max_length=10)
    donation_type = models.CharField("类型", max_length=1000)
    new = models.BooleanField("新/旧", default=False)
    number = models.IntegerField("数量", max_length=10)
    photo = models.ImageField(upload_to=get_upload_file_name,
                              help_text="Upload a zip file containing images, and they'll be imported into this gallery.")
    description = models.TextField("简介")
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def get_photo_url(self):
        print (self.photo.url)
        return self.photo.url

admin.site.register(Note)