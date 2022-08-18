import numpy as np
from django.db.models import Sum, F, Window, Func
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from . import models
from .forms import TaskForm, UpdateTaskForm
from .models import *
import logging


# Create your views here.


@never_cache
def Home(request):
    context = {
        "name": {"Home Farm Page"},
        'form': TaskForm
    }
    return render(request, 'mogoon/home.html', context)


@never_cache
def Notes(request):
    crop_today = Crop.objects.count()
    crop_todate = Crop.objects.aggregate(all_sum=Sum('crop_today'))
    plucker_numbers = Crop.objects.aggregate(all_quantity=Sum('plucker_numbers'))
    plucking_average = F(crop_today) / F(plucker_numbers)
    total_crop = Crop.objects.aggregate(total_sum=Sum('crop_todate'))
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
    # next_row = Crop.objects.get(id__gt=Crop.objects.id)
    # next_plucking_date = next_row.plucking_date
    crop_todate = Crop.objects.aggregate(all_sum=Sum('crop_today'))
    print(data)

    # crop_todate = Crop.objects.filter(
    #     Crop_today=data.id,
    #     date__range=(plucking_date, next_plucking_date)
    # ).order_by('id').annotate(
    #     cumbalance=Window(Sum('crop_today'), order_by=F('id').asc())
    # )
    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger('mogoon')
    # logger.info(data)
    logging.warning(data)
    plucker_numbers = Crop.objects.aggregate(all_quantity=Sum('plucker_numbers'))
    plucking_average = F(crop_today) / F(plucker_numbers)
    total_crop = Crop.objects.aggregate(total_sum=Sum('crop_todate'))

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
def mogoonCreate(request):
    if request.method == "POST":
        # Handle the form here
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mogoon/table.html')

        else:
            form = TaskForm()

        context = {
            'form': form, 'TaskForm': TaskForm,
        }
        plucking_date = request.POST['plucking_date']
        crop_data = request.POST['crop_data']
        crop_today = request.POST['crop_today']
        crop_todate = request.POST['crop_todate']
        plucker_number = request.POST['plucker_number']
        plucking_average = request.POST['plucking_average']
        total_crop = request.POST['total_crop']

        insert = Crop(plucking_date=plucking_date, crop_data=crop_data, crop_today=crop_today, crop_todate=crop_todate,
                      plucker_numbers=plucker_number, plucking_average=plucking_average, total_crop=total_crop)
        insert.save()
        return redirect('mogoon-table')
