from django.contrib import admin

from departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Поля в административной панели."""

    list_display = (
        "id",
    )
    list_filter = ("id",)
    search_fields = ("id",)
