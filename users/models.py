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

    USERNAME_FIELD = "email"  # используем почту, как основное поле (обязательное для ввода)
    REQUIRED_FIELDS = []  # можно добавить дополнительные поля

    #  генерация секретного токена
    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self):
        """Метод для строкового представления объекта пользователя (User)."""

        return f"{self.email}"

    class Meta:
        """Мета-информация модели User."""

        verbose_name = "Зарегистрированный пользователь"
        verbose_name_plural = "Зарегистрированные пользователи"
        ordering = ["id"]
