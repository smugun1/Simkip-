from datetime import datetime

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


def Logout(request):
    context = {
        "name": {"Logout"},

    }
    return render(request, 'mogoon/logout.html', context)


@never_cache
def CropTable(request):
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
def CropTableUpdate(request):
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
def mogoonCropCreate(request):
    if request.method == "POST":
        # this function saves a new record from the notes form. The crop_todate is the crop todate gotten from the
        # form(that was passed from the notes function) plus the crop today entered in the form.
        # Initially the crop to date is zero when the dta base is empty. the new crop to date will be zero plus the crop
        # today entered in the form, this addition is inserted and saved in the database as crop todate as shown below.
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

    return redirect('/crop_table')


@never_cache
def KandojobsTable(request):
    data = Kandojobs.objects.all()
    pruning_done = models.DateTimeField()
    pruned_block_No = models.IntegerField()
    pruned_bushes = Kandojobs.objects.count()
    pruning_cost = F(pruned_bushes) * F(input('pruning_rate'))
    weeding_done = models.DateTimeField()
    chemical_name = models.CharField()
    block_No = models.IntegerField()
    cost_per_lit = input('cost_per_unit')
    weeding_chem_amt = models.FloatField()
    weeding_labour = F(input('labour_number') * F(input('labour_cost')))
    weeding_cost = F(weeding_chem_amt) * (input(cost_per_lit))

    context = {
        "name": {"Kandojobs Table"},
        "kandojobs": data,
        "p_done": pruning_done,
        "p_block_No": pruned_block_No,
        "p_bushes": pruned_bushes,
        "P_cost": pruning_cost,
        "w_done": weeding_done,
        "c_name": chemical_name,
        "b_No": block_No,
        "c_per_lit": cost_per_lit,
        "w_chem_amt": weeding_chem_amt,
        "w_labour": weeding_labour,
        "w_cost": weeding_cost,
    }
    return render(request, 'mogoon/kandojobs_table.html', context)


@never_cache
def KandojobsTableUpdate(request):
    pruned_bushes = Kandojobs.objects.count()

    pruning_cost = F(pruned_bushes) * F(input('pruning_rate'))
    block_No = models.IntegerField()
    cost_per_lit = input()
    weeding_chem_amt = models.FloatField()
    weeding_labour = F(input('labour_number') * F(input('labour_cost')))

    weeding_cost = F(weeding_chem_amt) * (input(cost_per_lit))
    context = {
        "pruned_bushes": pruned_bushes,
        "pruning_cost": pruning_cost,
        "block_No": block_No,
        "cost_per_lit": cost_per_lit,
        "weeding_labour": weeding_labour,
        "weeding_chem_amt": weeding_chem_amt,
        "weeding_cost": weeding_cost,

        "name": {"Farm data Notes"},

    }
    return render(request, 'mogoon/kandojobs_table_update.html', context)


@never_cache
def mogoonKandojobsCreate(request):
    if request.method == "POST":
        pruned_block_No = request.POST['pruned_block_No']
        pruned_bushes = request.POST['pruned_bushes']
        pruning_done = request.POST['pruning_done']
        pruning_cost = request.POST['pruning_cost']
        weeding_done = request.POST['weeding_done']
        chemical_name = request.POST['chemical_name']
        block_No = request.POST['block_No']
        cost_per_lit = request.POST['cost_per_lit']
        weeding_chem = request.POST['weeding_chem']
        weeding_labour = request.POST['weeding_labour']
        weeding_cost = request.POST['weeding_cost']

        insert = Kandojobs(pruned_block_No=pruned_block_No, pruned_bushes=pruned_bushes, pruning_done=pruning_done,
                           pruning_cost=pruning_cost,
                           weeding_done=weeding_done, chemical_name=chemical_name, block_No=block_No,
                           cost_per_lit=cost_per_lit, weeding_chem=weeding_chem, weeding_labour=weeding_labour,
                           weeding_cost=weeding_cost)
        insert.save()
        return redirect('/kandojobs_table')


@never_cache
def MilkTable(request):
    data = Milk.objects.all()
    milking_done = models.DateTimeField()
    milk_today = Milk.objects.count()
    milk_todate = Milk.objects.aggregate(all_sum=Sum('milk_today'))
    cows_milked = Milk.objects.count()
    cow_numbers = Milk.objects.count()
    milking_average = F(milk_today) / F(cow_numbers)
    total_milk = Milk.objects.aggregate(total_sum=Sum('milk_todate'))
    calf_down = models.DateTimeField()
    calf_numbers = Milk.objects.count()
    vet_cost = models.FloatField()

    context = {
        "name": {"Milk Table"},
        "milk": data,
        "m_done": milking_done,
        "m_today": milk_today,
        "m_todate": milk_todate,
        "c_milked": cows_milked,
        "c_numbers": cow_numbers,
        "m_average": milking_average,
        "t_milk": total_milk,
        "cf_down": calf_down,
        "cf_numbers": calf_numbers,
        "v_cost": vet_cost,
    }
    return render(request, 'mogoon/milk_table.html', context)


@never_cache
def MilkTableUpdate(request):
    # get the current milk_todate value
    milk_todate = Milk.objects.aggregate(all_sum=Sum('milk_today'))

    # the milk_todate variable is a dictionary with a key value pair, the key is all_sum as set above,
    # when the database is empty the value of all_sum is set to python type called None, to cater for this scenario
    # get the value of the all_sum and check if it is nul as shown below, when null is set to type None and not type
    # Null
    if milk_todate.get('all_sum') is None:
        # if the value is of type None set the value to zero because this value is used later for additions and a none
        # type cannot be added to the int type
        milk_todate['all_sum'] = 0
        # this value appears in the form as 0 instead of 'None'
    else:
        # if it has an actual value get the milk_todate and pass it to the templates via the context, this value
        # appears in the form
        milk_todate = Milk.objects.aggregate(all_sum=Sum('milk_today'))

    context = {
        "milk_todate": milk_todate,
        "name": {"Milk table Update"},

    }
    return render(request, 'mogoon/milk_table_update.html', context)


@never_cache
def mogoonMilkCreate(request):
    if request.method == "POST":
        # this function saves a new record from the notes form. The milk_todate is the milk todate gotten from the
        # form(that was passed from the notes function) plus the milk today entered in the form.
        # Initially the crop to date is zero when the dta base is empty. the new milk to date will be zero plus the crop
        # today entered in the form, this addition is inserted and saved in the database as crop todate as shown below.
        milking_done = request.POST['milking_done']
        milk_today = request.POST['milk_today']
        milk_todate = int(request.POST['milk_todate']) + int(milk_today)
        # Initially request.POST['milk_today'] is a string, it has to be wrapped with an int for purpose of addition
        cows_milked = request.POST['cows_milked']
        cow_numbers = request.POST['cow_numbers']
        milking_average = request.POST['milking_average']
        total_milk = request.POST['total_milk']
        calf_down = request.POST['calf_down']
        calf_numbers = request.POST['calf_numbers']
        vet_cost = request.POST['vet_cost']

        insert = Milk(milking_done=milking_done, milk_today=milk_today, milk_todate=milk_todate,
                      cows_milked=cows_milked,
                      cow_numbers=cow_numbers, milking_average=milking_average, total_milk=total_milk,
                      calf_down=calf_down, calf_numbers=calf_numbers, vet_cost=vet_cost)
        insert.save()
        return redirect('/milk_table')


@never_cache
def FertilizerTable(request):
    data = Fertilizer.objects.all()
    fertilizer_applied = models.DateTimeField()
    fertilizer_amt = Fertilizer.objects.count()
    fertilizer_labour = Fertilizer.objects.aggregate(all_sum=Sum(input('labour')))
    fertilizer_cost = F(fertilizer_amt) * F(cost=5400) + F(input('labour') * 300)

    context = {
        "name": {"Fertilizer Table"},
        "fertilizer": data,
        "fertilizer_applied": fertilizer_applied,
        "fertilizer_amt": fertilizer_amt,
        "fertilizer_labour": fertilizer_labour,
        "fertilizer_cost": fertilizer_cost,

    }
    return render(request, 'mogoon/fertilizer_table.html', context)


@never_cache
def mogoonFertilizerTableUpdate(request):
    fertilizer_amt = Fertilizer.objects.count()
    context = {
        "fertilizer_amt": fertilizer_amt,
        "name": {"Fertilizer Table"},

    }
    return render(request, 'mogoon/fertilizer_table_update.html', context)


@never_cache
def mogoonFertilizerCreate(request):
    if request.method == "POST":
        fertilizer = request.POST['fertilizer']
        fertilizer_applied = request.POST['fertilizer_applied']
        fertilizer_amt = request.POST['fertilizer_amt']
        fertilizer_labour = request.POST['fertilizer_labour']
        fertilizer_cost = request.POST['fertilizer_cost']
        insert = Fertilizer(fertilizer=fertilizer, fertilizer_applied=fertilizer_applied, fertilizer_amt=fertilizer_amt,
                            fertilizer_labour=fertilizer_labour,
                            fertilizer_cost=fertilizer_cost)
        insert.save()
        return redirect('/fertilizer_table')


@never_cache
def update(request, pk):
    data = Crop.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/crop_table')

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
