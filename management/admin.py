from django.contrib import admin
from .models import Client, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'comment',)
    list_filter = ('name',)
    search_fields = ('email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_subject', 'message_body',)
    list_filter = ('message_subject',)
    search_fields = ('message_subject',)
