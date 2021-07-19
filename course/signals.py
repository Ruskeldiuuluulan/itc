from datetime import date
from django.db.models.signals import post_save
from course.models import Student
from django.dispatch import receiver


@receiver([post_save], sender=Student)
def my_signal(sender,instance,created,**kwargs):
    if created:
        current_date = date.today()
        current_year = current_date.year
        age = current_year - instance.date_of_birth.year
        instance.age = age
        instance.save()
        






