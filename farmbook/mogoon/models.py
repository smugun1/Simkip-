from django.db import models


# Create your models here.


class Crop(models.Model):
    CROP = [
        ('crop_today', (
            ('greentea', 'Greentea'),
            ('purpletea', 'Purpletea'),
        )
         ),
    ]
    plucking_date = models.DateTimeField(auto_now_add=False, blank=False)
    crop_data = models.CharField(max_length=50, choices=CROP, default=False)
    crop_today = models.IntegerField()
    crop_todate = models.IntegerField(null=True, blank=True)
    plucker_numbers = models.IntegerField()
    plucking_average = models.IntegerField(null=True, blank=True)
    total_crop = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.crop_data)


class Kandojobs(models.Model):
    pruning_done = models.DateTimeField(auto_now_add=False)
    pruned_block_No = models.IntegerField()
    pruned_bushes = models.IntegerField()
    pruning_rate = models.DecimalField(max_digits=4, decimal_places=2, default=None)
    pruning_cost = models.DecimalField(max_digits=8, decimal_places=2)
    weeding_done = models.DateTimeField(auto_now_add=False, default=None)
    chemical_name = models.CharField(max_length=100, default=None)
    block_No = models.IntegerField(name=None, default=None)
    cost_per_lit = models.DecimalField(max_digits=8, decimal_places=2)
    weeding_chem_amt = models.DecimalField(max_digits=8, decimal_places=2)
    weeding_labour_number = models.IntegerField(name=None, default=None)
    weeding_labour_rate = models.DecimalField(max_digits=8, decimal_places=2, default=None)
    weeding_labour = models.IntegerField(name=None, default=None)
    weeding_cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.pruned_bushes)


class Fertilizer(models.Model):
    fertilizer = models.CharField(max_length=20)
    fertilizer_applied = models.DateTimeField(auto_now_add=False)
    fertilizer_amt = models.DecimalField(max_digits=8, decimal_places=2)
    fertilizer_labour_rate = models.DecimalField(max_digits=8, decimal_places=2, default=None)
    fertilizer_labour = models.IntegerField()
    fertilizer_price = models.DecimalField(max_digits=8, decimal_places=2, default=None)
    fertilizer_cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.fertilizer_amt)


class Milk(models.Model):
    milking_done = models.DateTimeField(auto_now_add=False)
    milk_today = models.DecimalField(max_digits=8, decimal_places=2)
    milk_todate = models.DecimalField(max_digits=8, decimal_places=2)
    cows_milked = models.IntegerField()
    cow_numbers = models.IntegerField()
    milking_average = models.DecimalField(max_digits=4, decimal_places=2)
    total_milk = models.DecimalField(max_digits=8, decimal_places=2)
    calf_down = models.DateTimeField(auto_now_add=False)
    calf_numbers = models.IntegerField(blank=True)
    vet_cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    Total_vet_cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def __str__(self):
        return str(self.milk_today)
