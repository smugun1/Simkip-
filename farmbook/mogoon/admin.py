from django.contrib import admin
from .models import Crop, Kandojobs, Fertilizer, Milk

# Register your models here.

admin.site.register(Crop)
admin.site.register(Kandojobs)
admin.site.register(Fertilizer)
admin.site.register(Milk)


