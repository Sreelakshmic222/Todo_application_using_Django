from django.contrib import admin
from .models import Tasks,Login,Register

# Register your models here.
admin.site.register(Tasks)
admin.site.register(Login)
admin.site.register(Register)