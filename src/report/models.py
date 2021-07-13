from django.db import models

class customers(models.Model):
    Company_name = models.CharField(max_length=20)
    Contact_person = models.CharField(max_length=20)
    Mobile_number = models.CharField(max_length=10)

    def __str__(self):
        return self.Company_name
