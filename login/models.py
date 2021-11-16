from django.db import models

# Create your models here.
# Null = True => champ obligatoire


class Contact(models.Model):
    name = models.CharField(max_length = 100, null = True)
    job = models.CharField(max_length = 150, blank = True, null = True)
    phone = models.CharField(max_length = 100, null = True)
    mobile = models.CharField(max_length = 100, blank = True, null = True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.name
