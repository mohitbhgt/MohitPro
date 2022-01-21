# Generated by Django 4.0.1 on 2022-01-20 12:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_name', models.CharField(max_length=200)),
                ('student_class', models.CharField(max_length=10)),
                ('student_gender', models.CharField(max_length=20)),
                ('emp_enrollment_id', models.IntegerField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
