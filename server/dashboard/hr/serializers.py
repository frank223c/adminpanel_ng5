# -.- coding: utf-8 -.-
from rest_framework import serializers, pagination
from rest_framework_recursive.fields import RecursiveField
from .models import *
from dashboard.util.serializers import DynamicFieldModelSerializer
from dashboard.core.serializers import TownSerializer

class MemberSerializer(DynamicFieldModelSerializer):
		
	town_data = TownSerializer(source="town",many=False, required=False, read_only=True, fields=("id","name"))
	
	class Meta:
		model = Member
		fields = (	'id',
					'first_name',
					'last_name',
					'phone',
					'email',
					'town','town_data'
				)
	
