# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers


from .views import *

router = routers.DefaultRouter()
router.register(r'project', ProjectView)
router.register(r'flow_step', FlowStepView)
router.register(r'task', TaskView)
router.register(r'comment', CommentView)


urlpatterns = [
	url(r'^', include(router.urls)),
]
