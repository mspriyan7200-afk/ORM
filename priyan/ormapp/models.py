
from django.db import models
from django.contrib import admin
class product(models.Model):
    Name=models.CharField(max_length=100)
    Reference_Id=models.IntegerField(primary_key=True)
    Category=models.CharField(max_length=100)
    Date_Of_Manufacture=models.DateField()
    Colour=models.CharField(max_length=50)
    Max_Retail_Price=models.FloatField()
    Feedback=models.TextField()

class productAdmin(admin.ModelAdmin):
    list_display=["Name","Reference_Id","Category","Date_Of_Manufacture","Colour","Max_Retail_Price"]
