from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    age = models.PositiveIntegerField(null=True, blank=True)
    birth_date = models.DateField()    

    def __str__(self):
        return self.name + " " + self.last_name