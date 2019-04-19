from django.contrib import admin
from .models import Teacher, SRecord, Student, Course, CRecord, Learn

# Register your models here.
admin.site.site_header = u"考勤系统后台管理"

class TeatherAdmin(admin.ModelAdmin):
    list_display = ['t_id', 't_name', 't_password']
    # 每页10个
    list_per_page = 20

class CourseAdmin(admin.ModelAdmin):
    list_display = ['c_id', 'c_name', 't_id', 'week']
    # 每页10个
    list_per_page = 20


class LearnAdmin(admin.ModelAdmin):
    list_display = ['s_id', 'c_name']
    # 每页10个
    list_per_page = 20

class CRecordAdmin(admin.ModelAdmin):
    list_display = ['c_id','c_name', 'notcome', 'date','totalnum','realnum']
    # 每页10个
    list_per_page = 20

class SRecordAdmin(admin.ModelAdmin):
    list_display = ['s_id','c_id','c_name', 'num']
    # 每页10个
    list_per_page = 20


class StudentAdmin(admin.ModelAdmin):

    list_display = ('s_id', 's_name', 's_password',)

    list_per_page = 20


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeatherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CRecord, CRecordAdmin)
admin.site.register(SRecord, SRecordAdmin)
admin.site.register(Learn, LearnAdmin)
