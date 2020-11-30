from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=80)
    
    
    #products = models.ManyToManyField(Product, blank = True)
    #parent = models.ForeignKey(self, blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
