from django.db import models


class Client(models.Model):
    email = models.CharField(unique=True, max_length=100, verbose_name='Email')
    name = models.CharField(max_length=100, verbose_name='Ф.И.О')
    comment = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    message_subject = models.CharField(max_length=100, verbose_name="Тема")
    message_body = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return self.message_subject

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
