from django.forms import ModelForm

from management.models import Client, Message


class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя клиента'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите email клиента'
        })

        self.fields['comment'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Комментарий к клиенту'
        })


class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['message_subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите тему сообщения'
        })

        self.fields['message_body'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите сообщение'
        })
