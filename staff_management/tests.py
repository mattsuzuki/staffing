from django.test import TestCase
from .models import StaffMember
from django.contrib.auth.models import User


class StaffMemberModelTest(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(
            username='testuser', password='12345')  # Create a test User instance
        StaffMember.objects.create(
            user=test_user,  # Assign the test User instance to the user field
            job_title='Nurse',
            phone_number='1234567890',
            availability={'Monday': '9am-5pm', 'Tuesday': '9am-5pm'},
        )

    def test_staff_member_creation(self):
        self.assertEqual(StaffMember.objects.count(), 1)
        staff_member = StaffMember.objects.first()
        self.assertEqual(staff_member.user.username, 'testuser')
        self.assertEqual(staff_member.job_title, 'Nurse')
        self.assertEqual(staff_member.phone_number, '1234567890')
        self.assertEqual(staff_member.availability, {
            'Monday': '9am-5pm', 'Tuesday': '9am-5pm'})
