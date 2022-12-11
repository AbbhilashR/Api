from django.contrib import admin
from .models import booking,car,user
# Register your models here.
admin.site.register(user)
admin.site.register(car)
admin.site.register(booking)