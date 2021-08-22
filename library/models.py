from django.db import models

class Book(models.Model):
    title = models.CharField (max_length = 255)
    author = models.CharField (max_length = 255)
    ISBN = models.CharField (max_length = 50, unique=True)
    Edution= models.CharField(max_length = 255)
    record_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()

    def __str__(self):
        return self.title