from django.db import models


class Department(models.Model):
    """Поля для модели профиля пользователя."""

    class Meta:
        """Мета-информация модели User."""

        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
