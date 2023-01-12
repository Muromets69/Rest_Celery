from django.db import models

class Car(models.Model):
    name = models.CharField("Name",max_length=50)
    img = models.ImageField("Image",upload_to="auto/")