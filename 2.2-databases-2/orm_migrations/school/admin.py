from django.contrib import admin

from .models import Student, Teacher, StudentTeacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "group"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "subject"]


@admin.register(StudentTeacher)
class StudentTeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "student_id", "teacher_id"]