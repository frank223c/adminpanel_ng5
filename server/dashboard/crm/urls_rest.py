# -*- coding: utf-8 -*-

from django.conf.urls import  url, include
from rest_framework import routers


from .views import *

router = routers.DefaultRouter()
router.register(r'customer', CustomerView)

urlpatterns = [	
	url(r'^', include(router.urls)),
]
