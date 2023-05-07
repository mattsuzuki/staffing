# Generated by Django 4.1.5 on 2023-05-07 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="StaffMember",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("job_title", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=15)),
                ("availability", models.JSONField(default=dict)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Shift",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "shift_type",
                    models.CharField(
                        choices=[
                            ("AM", "Morning"),
                            ("PM", "Afternoon"),
                            ("NIGHT", "Night"),
                        ],
                        max_length=10,
                    ),
                ),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                (
                    "staff_member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff_management.staffmember",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShiftPreference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "preferred_shift",
                    models.CharField(
                        choices=[
                            ("AM", "Morning"),
                            ("PM", "Afternoon"),
                            ("NIGHT", "Night"),
                        ],
                        max_length=10,
                    ),
                ),
                ("priority", models.PositiveIntegerField()),
                (
                    "staff_member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff_management.staffmember",
                    ),
                ),
            ],
            options={"unique_together": {("staff_member", "preferred_shift")},},
        ),
    ]