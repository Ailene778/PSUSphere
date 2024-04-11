from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

admin.site.register(College)
admin.site.register(Program)
admin.site.register(Organization)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname",)


@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined")
    search_fields = ("student__lastname", "student__firstname")

    def get_member_program(self, obj):
        return obj.student.program  # Access the program through obj.student

    get_member_program.short_description = "Program"  # Set a custom column header for the program


# Note: Make sure to update the search_fields to use double underscores for related fields like student__lastname and student__firstname.
