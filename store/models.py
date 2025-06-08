from django.db import models

# Create your models here.

class store(models.Model):
    book_id=models.IntegerField()
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    photo=models.CharField(max_length=300)
    year_of_pub=models.IntegerField()
    Total_copies=models.IntegerField()
    available_copies=models.IntegerField()
    shelf_location=models.CharField(max_length=100)
