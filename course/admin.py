from django.contrib import admin
from .models import Branch, Course, Group, Student


# Register your models here.

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
    list_filter = ('creator', 'manager')
    raw_id_fields = ('creator',)

admin.site.register(Branch,BranchAdmin)

admin.site.register(Group)

admin.site.register(Student)

admin.site.register(Course)

class MODEL_ADMIN(admin.ModelAdmin):
    class Media:
        css = {'all': ('css/no-addanother-button.css',)}