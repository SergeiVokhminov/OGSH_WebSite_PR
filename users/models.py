import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Поля для модели пользователя."""

    username = None  # отключаем использование username
    email = models.EmailField(unique=True, verbose_name="Электронная почта")  # почта уникальна
    token = models.CharField(
        max_length=64,
        verbose_name="Токен пользователя",
        unique=True,
    )  # секретный токен

    USERNAME_FIELD = "email"  # используем почту для входа
    REQUIRED_FIELDS = []

    #  генерация секретного токена
    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self):
        """Метод для строкового представления объекта User."""

        return f"{self.email}"

    class Meta:
        """Мета-информация модели User."""

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]
