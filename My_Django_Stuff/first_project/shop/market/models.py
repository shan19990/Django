from django.db import models

class marketItems(models.Model):
    itemName = models.CharField(max_length=20)
    itemDescription = models.TextField(max_length=100)
    itemPrice = models.IntegerField()
    itemPic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.itemName