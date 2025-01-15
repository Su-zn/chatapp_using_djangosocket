from django.forms import ModelForm
from django import forms
from .models import *



class ChatmessageCreateForm(forms.ModelForm):
    class Meta:
        model=GroupMessage
        fields=['body']
        widgets={
            'body': forms.TextInput(attrs={'placeholder': 'Add messsage ....','class':'p-4 text-black','maxlength':'300','autofocous':'True'})
                                            },