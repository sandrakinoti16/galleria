from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image
from galleria.forms import SignUpForm
from django.contrib.auth import login, authenticate
# Create your views here.
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    categories = Category.objects.all()

    context = {}
    context['categories'] = categories

    return render(request, 'main/index.html', context)


def categoryPage(request, slug):

    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category).order_by('-date_created')[:6]
    for x in images:
        x.shortDescription = x.description[:130]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'main/category.html', context)


def imageDetailPage(request, slug1, slug2):

    category = Category.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)

    context = {}
    context['category'] = category
    context['image'] = image
    return render(request, 'main/image.html', context)

def category_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category_term = request.GET.get("image")
        searched_images = Image.search_by_category(category_term)

        message = f"{category_term}"

        return render(request,'galleries/search.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for an image yet"

        return render(request,'galleries/search.html',{"message":message})


def location_results(request):

    if 'image' in request.GET and request.GET["image"]:
        location_term = request.GET.get("image")
        searched_images = Image.search_by_location(location_term)

        message = f"{location_term}"

        return render(request,'main/search.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for an image yet"

        return render(request,'main/search.html',{"message":message})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
























###
