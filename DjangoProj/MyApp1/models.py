from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import RegexValidator


class teacher(models.Model):
    #two fields - 1 name and 1 for teaching area
      Name = models.CharField(max_length=25)
      Area = models.CharField(max_length=30)


class asset(models.Model): 
    name = models.CharField(max_length=100, primary_key=True)
    Qrcode = models.ImageField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos')
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    
    def __str__(self):
        return self.name

class Requests(models.Model):
    sendby = models.CharField(max_length=100)
    assetname = models.CharField(max_length=150)
    assetid = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r'^[a-zA-Z0-9]+$')])
    Status = (
        (0, 'not started'), 
        (1, 'in progress'), 
        (2, 'completed'), 
    )
    status = models.IntegerField(default=0, choices=Status)
    class Meta:
       verbose_name_plural = 'Requests'
    def __str__(self):
        return str(self.sendby)

class Repaired(models.Model):
    requests = models.ForeignKey(Requests, on_delete=models.CASCADE, null=True)
    sendby = models.CharField(max_length=300)
    assetname = models.CharField(max_length=150)
    assetid = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r'^[a-zA-Z0-9]+$')])
    
    class Meta:
       verbose_name_plural = 'Repaired'
    def __str__(self):
        return str(self.sendby)


class Overdue(models.Model):
    requests = models.ForeignKey(Requests, on_delete=models.CASCADE, null=True)
    sendby = models.CharField(max_length=300)
    assetname = models.CharField(max_length=150)
    assetid = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r'^[a-zA-Z0-9]+$')])
    class Meta:
        verbose_name_plural = 'Overdue'
    def __str__(self):
        return str(self.sendby)


