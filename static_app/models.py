from django.db import models


# Create table
class place(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class news(models.Model):
    head = models.CharField(max_length=50)
    sub_head = models.CharField(max_length=70)
    desc = models.TextField()
    img = models.ImageField(upload_to='picture')
    day = models.IntegerField()
    month = models.CharField(max_length=12)
