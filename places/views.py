from django.shortcuts import render, redirect
from . models import Place
from .forms import PlaceForm


def index(request):
    places = Place.objects.order_by('-date_posted')

    context = {'places': places}

    return render(request, 'places/index.html', context)


def add(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlaceForm()

    context = {'form': form}

    return render(request, 'places/add.html', context)
