from django import forms
from django.forms import ModelForm
from .models import Room, Message

class RoomForm(ModelForm):
    topic = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter a tag',
        'class': 'form-control'
    }))

    class Meta:
        model = Room
        fields = [ 'name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter room title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'room description'}),
        }


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

