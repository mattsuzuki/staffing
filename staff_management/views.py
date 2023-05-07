from rest_framework import generics
from .models import StaffMember
from .serializers import StaffMemberSerializer
from email import message_from_bytes

from email import message_from_bytes


class StaffMemberList(generics.ListCreateAPIView):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer
