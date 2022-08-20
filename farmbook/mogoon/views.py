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
def Crop_Table_Update(request):
    # get the current crop_todate value
    crop_todate = Crop.objects.aggregate(all_sum=Sum('crop_today'))

    # the crop_todate variable is a dictionary with a key value pair, the key is all_sum as set above,
    # when the database is empty the value of all_sum is set to python type called None, to cater for this scenario
    # get the value of the all_sum and check if it is nul as shown below, when null is set to type None and not type
    # Null
    if crop_todate.get('all_sum') is None:
        # if the value is of type None set the value to zero because this value is used later for additions and a none
        # type cannot be added to the int type
        crop_todate['all_sum'] = 0
        # this value appears in the form as 0 instead of 'None'
    else:
        # if it has an actual value get the crop_todate and pass it to the templates via the context, this value
        # appears in the form
        crop_todate = Crop.objects.aggregate(all_sum=Sum('crop_today'))
    context = {
        "crop_todate": crop_todate,
        "name": {"Farm data Notes"},

    }
    return render(request, 'mogoon/crop_table_update.html', context)


@never_cache
def Crop_Table(request):
    data = Crop.objects.all()
    plucking_date = models.DateTimeField()
    crop_today = Crop.objects.count()
    crop_todate = Crop.objects.aggregate(all_sum=Sum('crop_today'))
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
    return render(request, 'mogoon/crop_table.html', context)


# raise Exception("I want to know value" + str("Crop Table"))
@never_cache
def update(request, pk):
    data = Crop.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('mogoon/crop_table.html')

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
        return redirect('/table')

    context = {
        'item': data,
    }
    return render(request, 'Crop_data/delete.html', context)


@never_cache
def mogoonCreate(request):
    if request.method == "POST":
        # this function saves a new record from the notes form. The crop_todate is the crop todate gotten from the
        # form(that was passed from the notes function) plus the crop today entered in the form.
        # Initially the crop to date is zero when the dta base is empty. the new crop to date will be zero plus the
        plucking_date = request.POST['plucking_date']
        crop_data = request.POST['crop_data']
        crop_today = request.POST['crop_today']
        # Initially request.POST['crop_today'] is a string, it has to be wrapped with an int for purpose of addition
        crop_todate = int(request.POST['crop_todate']) + int(crop_today)
        plucker_number = request.POST['plucker_number']
        plucking_average = request.POST['plucking_average']
        total_crop = request.POST['total_crop']

        insert = Crop(plucking_date=plucking_date, crop_data=crop_data, crop_today=crop_today, crop_todate=crop_todate,
                      plucker_numbers=plucker_number, plucking_average=plucking_average, total_crop=total_crop)
        insert.save()
        return redirect('mogoon-table')


@never_cache
def KandojobsTable(request):
    job = Kandojobs.objects.all()
    pruned_block_No = models.IntegerField()
    pruned_bushes = models.IntegerField()
    pruning_done = models.DateTimeField()
    pruning_cost = models.FloatField()
    weeding_done = models.DateTimeField()
    chemical_name = models.CharField()
    block_No = models.IntegerField()
    weeding_chem = models.CharField()
    weeding_labour = models.IntegerField()
    weeding_cost = models.FloatField()

    context = {
        "name": {"Kandojobs Table"},
        "pruned_block_No": pruned_block_No,
        "pruned_bushes": pruned_bushes,
        "pruning_done": pruning_done,
        "Pruning_cost": pruning_cost,
        "weeding_done": weeding_done,
        "chemical_name": chemical_name,
        "block_No": block_No,
        "weeding_chem": weeding_chem,
        "weeding_labour": weeding_labour,
        "weeding_cost": weeding_cost,
    }
    return render(request, 'mogoon/kandojobs_table.html', context)


@never_cache
def MilkTable(request):
    lit = Milk.objects.all()
    milking_done = models.DateTimeField()
    milk_today = Milk.objects.count()
    milk_todate = Milk.objects.aggregate(all_sum=Sum('milk_today'))
    cows_milked = models.IntegerField()
    cows_numbers = Milk.objects.aggregate(all_quantity=Sum('cows_numbers'))
    milking_average = F(milk_today) / F(cows_numbers)
    total_milk = Milk.objects.aggregate(total_sum=Sum('milk_todate'))
    calf_down = models.DateTimeField()
    calf_numbers = Milk.objects.aggregate(all_quantity=Sum('cows_numbers'))
    vet_cost = models.FloatField()

    context = {
        "name": {"Milk Table"},
        "milking_done": milking_done,
        "milk_today": milk_today,
        "milk_todate": milk_todate,
        "cows_milked": cows_milked,
        "cows_numbers": cows_numbers,
        "milking_average": milking_average,
        "total_milk": total_milk,
        "calf_down": calf_down,
        "calf_numbers": calf_numbers,
        "vet_cost": vet_cost,
    }
    return render(request, 'mogoon/milk_table.html', context)


@never_cache
def Sign_Up_Table(request):
    context = {
        "name": {"Sign Up"},

    }
    return render(request, 'mogoon/sign_up.html', context)

@never_cache
def Sign_In_Table(request):
    context = {
        "name": {"Login"},

    }
    return render(request, 'mogoon/login.html', context)
