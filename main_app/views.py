from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Clothes


def home(request):
    return render(request, 'home.html')


def clothes_index(request):
    clothes = Clothes.objects.all()

    return render(request, 'clothes/index.html', {
        'clothes': clothes
    })

def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('clothing/index')

        else:
            error_message = 'Invalid sign up - try again.'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}

    return render(request, 'registration/signup.html', context)
