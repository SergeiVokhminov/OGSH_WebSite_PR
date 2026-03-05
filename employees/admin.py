from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Поля в административной панели."""

    list_display = (
        "id",
        "condition",
        "email",
        "first_name",
        "last_name",
        "position",
        "department",
        "phone_number",
    )
    list_filter = ("id", "condition","first_name", "last_name")
    search_fields = ("email", "first_name", "last_name")
