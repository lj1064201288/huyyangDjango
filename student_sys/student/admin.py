from django.contrib import admin

# Register your models here.

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex', 'profession', 'email',
                    'qq', 'phone', 'status', 'created_time']

    list_filter = ('sex', 'status', 'created_time')
    search_fields = ('name', 'profesion')
    fieldsets = [
        (None, {
            'fields': (
            'name',
            ('sex', 'profession'),
            ('email', 'qq', 'phone'),
            'status',
            )
        })
    ]