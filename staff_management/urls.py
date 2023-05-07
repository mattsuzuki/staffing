from django.urls import path
from . import views

urlpatterns = [
    path('staff_members/', views.StaffMemberList.as_view(),
         name='staff_member_list'),
]
