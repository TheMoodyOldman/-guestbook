from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import Message

# Create your views here.

class MsgList(ListView):
    model = Message
    ordering = ['id', 'time']

class MsgDetail(DetailView):
    model = Message

class MsgCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content']

    def get_success_url(self):
        return reverse_lazy('msglist_url')

class MsgDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('msglist_url')
