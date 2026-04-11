from django import forms

from departments.models import Department


class DepartmentForm(forms.ModelForm):
    """Форма представления работника."""

    class Meta:
        model = Department
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)


class DepartmentUpdateForm(forms.ModelForm):
    """Форма обновления данных работника."""

    class Meta:
        model = Department
        fields = (
            "name",
            "abbreviated_name",
            "phone",
        )
        widgets = {
            "condition": forms.Select(
                attrs={"class": "form-select"}
            ),  # Bootstrap стиль
        }

    def __init__(self, *args, **kwargs):
        super(DepartmentUpdateForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Название Отдела"}
        )
        self.fields["abbreviated_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Сокращенное название"}
        )
        self.fields["phone"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите номер телефона (только цифры)",
            }
        )
