from django.urls import path
from management.apps import ManagementConfig
from management.views import (HomeTemplateView, ClientListView, ClientCreateView, ClientDeleteView, ClientDetailView,
                              ClientUpdateView, MessageListView, MessageCreateView, MessageUpdateView,
                              MessageDetailView, MessageDeleteView)

app_name = ManagementConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('client_list', ClientListView.as_view(), name='client_list'),
    path('client_list/create', ClientCreateView.as_view(), name='client_create'),
    path('client_list/client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_list/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_list/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('message_list', MessageListView.as_view(), name='message_list'),
    path('message_list/create', MessageCreateView.as_view(), name='message_create'),
    path('message_list/client_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_list/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_list/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
]
