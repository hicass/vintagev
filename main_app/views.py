from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Clothes, Photo
import uuid
import boto3
import os



def home(request):
    return render(request, 'home.html')

@login_required
def bag(request):
  return render(request, 'bag.html')

@login_required
def likes(request):
  return render(request, 'likes.html')


def clothes_index(request):
    clothing = Clothes.objects.all()
    return render(request, 'clothes/index.html', {
        'clothing': clothing
    })


class ClothesCreate(LoginRequiredMixin, CreateView):
  model = Clothes
  fields = ['clothing_name', 'brand', 'category', 'size', 'condition', 'material', 'color', 'description', 'price']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return redirect(request, '/')


class ClothesUpdate(LoginRequiredMixin, UpdateView):
  model = Clothes
  fields = ['category', 'size', 'condition', 'material', 'color', 'price', 'brand', 'clothing_name', 'description']


class ClothesDelete(LoginRequiredMixin, DeleteView):
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





@login_required
def add_photo(request, clothes_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, clothes_id=clothes_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', clothes_id=clothes_id)



def clothes_detail(request, clothes_id):
    clothing = Clothes.objects.get(id=clothes_id)

    return render(request, 'clothes/detail.html', {
        'clothing': clothing
    })


