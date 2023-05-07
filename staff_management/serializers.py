from rest_framework import serializers
from .models import StaffMember


class StaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffMember
        fields = [
            'id',
            'user',
            'job_title',
            'phone_number',
            'availability',
            'additional_availability',
            'credentials',
            'preferred_unit',
            'schedule',
        ]
