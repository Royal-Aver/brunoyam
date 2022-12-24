from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import UserForm

def main_page(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'service/main.html', context)


class UsersRegistration(CreateView):
    template_name = 'service/main.html'
    form_class = UserForm
    success_url = reverse_lazy('index')


