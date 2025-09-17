from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()
    services = models.ManyToManyField(Service)
    
    def __str__(self):
        return self.name
    

# dashboard

class Pages(models.Model):
    page = models.CharField(max_length=100)
    def __str__(self):
        return self.page
class SubSection(models.Model):
    page_name = models.ForeignKey(Pages, on_delete=models.CASCADE)
    sub_page = models.CharField(max_length=100)
    def __str__(self):
        return self.sub_page