# Generated by Django 3.2.4 on 2021-06-28 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_student_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
    ]
