# -*- coding: utf8 -*-


# Copyright (c) 2019, Rectcircle. All rights reserved.
# @author Rectcircle
# @date 2019-06-12
# @version 0.0.1

from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
  url(r'^path/', admin.site.urls),
  # TODO: happy coding! (created by vscode extension new-file-by-type)
]
