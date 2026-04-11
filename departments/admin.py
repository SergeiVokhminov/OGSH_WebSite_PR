from django.contrib import admin

from departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Поля в административной панели."""

    list_display = (
        "id",
        "name",
        "abbreviated_name",
    )
    list_filter = ("id", "name",)
    search_fields = ("id", "abbreviated_name",)
