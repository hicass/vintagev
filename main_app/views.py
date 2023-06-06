from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')


def clothes_index(request):
    return render(request, 'clothes/index.html')


class ClothesCreate(CreateView):
  model = Clothes
  fields = ['Size', 'Condition', 'Material', 'Color', 'Brand', 'clothing_name', 'Description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)





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
