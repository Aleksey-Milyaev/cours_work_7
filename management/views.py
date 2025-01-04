from .models import Client, Message
from .forms import ClientForm, MessageForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, DetailView, UpdateView


class HomeTemplateView(TemplateView):
    template_name = "management/home.html"


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('management:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('management:client_list')


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('management:client_list')


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('management:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('management:message_list')


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('management:message_list')


