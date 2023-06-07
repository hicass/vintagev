from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Clothes


def home(request):
    return render(request, 'home.html')


def bag(request):
  return render(request, 'bag.html')

def likes(request):
  return render(request, 'likes.html')


def clothes_index(request):
    clothing = Clothes.objects.all()

    return render(request, 'clothes/index.html', {
        'clothing': clothing
    })


class ClothesCreate(CreateView):
  model = Clothes
  fields = ['clothing_name', 'brand', 'category', 'size', 'condition', 'material', 'color', 'description', 'price']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return redirect(request, '/')
  
class ClothesUpdate(UpdateView):
  model = Clothes
  fields = ['category', 'size', 'condition', 'material', 'color', 'price', 'brand', 'clothing_name', 'description']

class ClothesDelete(DeleteView):
  model = Clothes
#   success_url '/clothes'

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
