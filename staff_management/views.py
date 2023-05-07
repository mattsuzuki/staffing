from rest_framework import generics
from .models import StaffMember
from .serializers import StaffMemberSerializer


class StaffMemberList(generics.ListCreateAPIView):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer
