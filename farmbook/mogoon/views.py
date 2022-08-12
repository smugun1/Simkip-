from django.db.models import Sum, F
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from . import models
from .forms import TaskForm, UpdateTaskForm
from .models import *


# Create your views here.


@never_cache
def Home(request):
    context = {
        "name": {"Home Farm Page"},
        'form': TaskForm
    }
    return render(request, 'mogoon/home.html', context)


@never_cache
def Image(request):
    context = {
        "name": {"Farm images"},
    }
    return render(request, 'mogoon/image.html', context)


@never_cache
def Notes(request):
    crop_todate = Crop.objects.aggregate(all_sum=Sum('crop_today'))

    context = {
        "crop_todate": crop_todate,
        "name": {"Farm data Notes"},

    }
    return render(request, 'mogoon/notes.html', context)


@never_cache
def Table(request):
    data = Crop.objects.all()
    plucking_date = models.DateTimeField()
    crop_today = Crop.objects.count()
    crop_todate = Crop.objects.aggregate(all_sum=Sum('crop_today'))
    plucker_numbers = Crop.objects.aggregate(all_quantity=Sum('plucker_numbers'))
    plucking_average = F(crop_today) / F(plucker_numbers["all_quantity"])
    total_crop = Crop.objects.aggregate(all_sum=Sum('crop_todate'))

    context = {
        "name": {"Crop Table"},
        "crop_data": data,
        "plucking_date": plucking_date,
        "c_today": crop_today,
        "c_todate": crop_todate,
        "p_numbers": plucker_numbers,
        "p_average": plucking_average,
        "t_crop": total_crop,
    }
    return render(request, 'mogoon/table.html', context)


# raise Exception("I want to know value" + str("Crop Table"))
@never_cache
def update(request, pk):
    data = Crop.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('mogoon/table.html')

    else:
        form = UpdateTaskForm(instance=data)

    context = {
        'form': form, 'UpdateTaskForm': UpdateTaskForm,

    }
    return render(request, 'Crop_data/update.html', context)


@never_cache
def delete(request, pk):
    data = Crop.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('mogoon/table.html')

    context = {
        'item': data,
    }
    return render(request, 'Crop_data/delete.html', context)


@never_cache
def update_form(request, pk):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mogoon/table.html')

    else:
        form = TaskForm()

    context = {
        'form': form, 'TaskForm': TaskForm,
    }
    return render(request, 'Crop_data/update_form.html', context)


def mogoonCreate(request):
    if request.method == "POST":
        # Handle the form here
        plucking_date = request.POST['plucking_date']
        crop_data = request.POST['crop_data']
        crop_today = request.POST['crop_today']
        crop_todate = request.POST['crop_todate']
        plucker_number = request.POST['plucker_number']
        pluckin_avaerage = request.POST['plucking_average']
        total_crop = request.POST['total_crop']

        insert = Crop(plucking_date=plucking_date, crop_data=crop_data, crop_today=crop_today, crop_todate=crop_todate,
                      plucker_number=plucker_number, pluckin_avaerage=pluckin_avaerage, total_crop=total_crop)
        insert.save()
        return redirect('mogoon-table')
