from django.contrib import admin

# Register your models here.

from .models import Contact, Ville

admin.site.register(Contact)
admin.site.register(Ville)