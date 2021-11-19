from django.db import models


# Create your models here.
# Blank = False => champ obligatoire (valeur par défaut)

# Si many to many Django créera une table intermédiaire pour faire correspondre les id des deux tables =

# One -> Many : Ville -> Etablissement
# One -> Many : Etablissement -> Contact

class Contact(models.Model):
    nom = models.CharField(max_length = 100, null = True)
    emploi = models.CharField(max_length = 150, blank = True, null = True)
    mail = models.EmailField(max_length = 250, blank = True)
    tel = models.CharField(max_length = 12, null = True)
    mobile = models.CharField(max_length = 12, blank = True, null = True)
    date_ajout= models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.nom


class Ville(models.Model):
    nom = models.CharField(max_length = 100, null = True)
    localisation = models.ImageField\
        (upload_to = "static/images/locations",
         height_field = 100,
         width_field = 200,
         max_length = 100,
         blank = True,
         null = True)
    population = models.PositiveIntegerField()
    contact = models.ForeignKey(Contact, null = True, on_delete = models.SET_NULL)
    date_ajout = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.nom


class Etablissement(models.Model):
    DISPONIBILITE = (
        ('Disponible', 'Disponible'),
        ('Indisponible', 'Indisponible'),
    )
    nom = models.CharField(max_length= 200)
    superficie = models.FloatField()
    date_ajout = models.DateTimeField(auto_now_add = True, null = True)
    ville = models.ForeignKey(Ville, null = True, on_delete = models.SET_NULL)
    
    
    def __str__(self):
        return self.nom