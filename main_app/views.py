from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import Context
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
    clothing = Clothes.objects.all().order_by('-id')

    return render(request, 'clothes/index.html', {
        'clothing': clothing,
        'category': 'All'
    })


def tops_index(request):
    clothing = Clothes.objects.filter(category='T').order_by('-id')

    return render(request, 'clothes/index.html', {
        'clothing': clothing,
        'category': 'Tops!'
    })


def bottoms_index(request):
    clothing = Clothes.objects.filter(category='Btm').order_by('-id')

    return render(request, 'clothes/index.html', {
        'clothing': clothing,
        'category': 'Bottoms!'
    })


def jackets_index(request):
    clothing = Clothes.objects.filter(category='Jckt').order_by('-id')

    return render(request, 'clothes/index.html', {
        'clothing': clothing,
        'category': 'Jackets'
    })


def dresses_index(request):
    clothing = Clothes.objects.filter(category='Drs').order_by('-id')

    return render(request, 'clothes/index.html', {
        'clothing': clothing,
        'category': 'Dresses!'
    })


def jumpsuits_index(request):
    clothing = Clothes.objects.filter(category='Jmp').order_by('-id')

    return render(request, 'clothes/index.html', {
        'clothing': clothing,
        'category': 'Jumpsuits!'
    })


def shoes_index(request):
    clothing = Clothes.objects.filter(category='Sh').order_by('-id')

    return render(request, 'clothes/index.html', {
        'clothing': clothing,
        'category': 'Shoes'
    })


def accessories_index(request):
    clothing = Clothes.objects.filter(category='Acc').order_by('-id')

    return render(request, 'clothes/index.html', {
        'clothing': clothing,
        'category': 'Accessories!'
    })


def clothes_detail(request, clothes_id):
    clothes = Clothes.objects.get(id=clothes_id)

    return render(request, 'clothes/detail.html', {
        'clothes': clothes
    })


class ClothesCreate(LoginRequiredMixin, CreateView):
    model = Clothes
    fields = ['clothing_name', 'brand', 'category', 'size', 'condition', 'material', 'color', 'description', 'price',]

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class ClothesUpdate(LoginRequiredMixin, UpdateView):
  model = Clothes
  fields = ['category', 'size', 'condition', 'material', 'color', 'price', 'brand', 'clothing_name', 'description']


class ClothesDelete(LoginRequiredMixin, DeleteView):
  model = Clothes
  success_url = '/clothing'


def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')

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
            Photo.objects.create(url=url, clothing_id=clothes_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', clothes_id=clothes_id)