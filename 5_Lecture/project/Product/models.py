from django.db import models

# Create your models here.
class product(models.Model):
    Name = models.CharField(max_length = 20)
    Price = models.IntegerField()
    Category = models.CharField(max_length=15, default="General")

    def __str__(self):
        return self.Name
    