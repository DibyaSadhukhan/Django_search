from django.db import models

# Create your models here.
class resturant_details(models.Model):
    ID=models.IntegerField(primary_key=True)
    Resturant_Name=models.CharField(max_length=255)
    Location=models.CharField(max_length=255,default=None, blank=True, null=True)
    Latitude=models.CharField(max_length=255,default=None, blank=True, null=True)
    Longitude=models.CharField(max_length=255,default=None, blank=True, null=True)
    Rating= models.FloatField(default=None, blank=True, null=True)
    No_of_votes= models.IntegerField(default=None, blank=True, null=True)
    True_rating= models.FloatField(default=None, blank=True, null=True)
    # (max_length=255,default=None, blank=True, null=True)
    def __str__(self):
        return self.Resturant_Name


class menu_details(models.Model):
    ID=models.BigAutoField(primary_key=True)
    Item=models.CharField(max_length=255,default=None, blank=True, null=True)
    Item_det=models.CharField(max_length=255,default=None, blank=True, null=True)
    Price=models.CharField(max_length=255,default=None, blank=True, null=True)
    Resturant=models.ForeignKey(resturant_details,on_delete=models.CASCADE,related_name='resturant',default=1)
    def __str__(self):
        return self.Item

class menu_items(models.Model):
    ID=models.BigAutoField(primary_key=True)
    Item_name=models.CharField(max_length=255,default=None, blank=True, null=True)
    Count=models.IntegerField(default=None,blank=True,null=True)
    def __str__(self):
        return self.Item_name



