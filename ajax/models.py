from django.db import models
from django.forms import ImageField


class FileUpload(models.Model):


    file = models.ImageField(upload_to ='files/')

