from django.db import models


# Create your models here.
# Null = True => champ obligatoire


class Contact(models.Model):
    name = models.CharField(max_length = 100, null = True)
    job = models.CharField(max_length = 150, blank = True, null = True)
    email = models.EmailField(max_length = 250, blank = True)
    phone = models.CharField(max_length = 12, null = True)
    mobile = models.CharField(max_length = 12, blank = True, null = True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Ville(models.Model):
    name = models.CharField(max_length = 100, null = True)
    location = models.ImageField\
        (upload_to = "static/images/locations",
         height_field = 100,
         width_field = 200,
         max_length = 100,
         blank = True,
         null = True)
    population = models.PositiveIntegerField()
    contact = Contact()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    