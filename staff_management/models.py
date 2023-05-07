from django.db import models
from django.contrib.auth.models import User


class StaffMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    availability = models.JSONField(default=dict)  # Example: {'Monday': '9am-5pm', 'Tuesday': '9am-5pm', ...}
    
    def __str__(self):
        return self.user.get_full_name()


class Shift(models.Model):
    SHIFT_TYPES = [
        ('AM', 'Morning'),
        ('PM', 'Afternoon'),
        ('NIGHT', 'Night'),
    ]

    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    shift_type = models.CharField(max_length=10, choices=SHIFT_TYPES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.staff_member} - {self.get_shift_type_display()} shift"


class ShiftPreference(models.Model):
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    preferred_shift = models.CharField(max_length=10, choices=Shift.SHIFT_TYPES)
    priority = models.PositiveIntegerField()

    class Meta:
        unique_together = ('staff_member', 'preferred_shift')

    def __str__(self):
        return f"{self.staff_member} - {self.get_preferred_shift_display()} preference"

