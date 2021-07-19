from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields.json import HasAnyKeys
from django.urls import reverse
from django.conf import settings

class Branch(models.Model):
    class Meta:
        verbose_name = 'филиал'
        verbose_name_plural = 'филиалы'
    
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=300, null=True)
    photo = models.ImageField(upload_to='branches/', null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,null=True, related_name='branches')
    manager = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.PROTECT)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("branch_detail", kwargs={"branch_id": self.pk})
    
    
    

class Group(models.Model):
    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
    
    name = models.CharField(max_length=100, null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='group_list/', null=True, blank=True)
    
    course = models.ForeignKey('course.Course', on_delete=models.PROTECT,null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, related_name='my_groups')
    manager = models.OneToOneField(settings.AUTH_USER_MODEL,null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.name

class Student(models.Model):
    
    MALE = 'male'
    FEMALE = 'female'
    
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
    
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6, default=MALE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='student_list/', null=True, blank=True)
    courses = models.ManyToManyField(Course)
    age = models.PositiveIntegerField(null=True)


    def __str__(self):
        return self.name




    