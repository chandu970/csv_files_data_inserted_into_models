from django.db import models

# Create your models here.

class Banks(models.Model):
    bank_name=models.CharField(max_length=100)

    def __str__(self):
        return self.bank_name

class Branches(models.Model):
    bank_name=models.ForeignKey(Banks,on_delete=models.CASCADE)
    IFSC=models.TextField(max_length=50,primary_key=True,unique=True)
    branch_name=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    contact=models.IntegerField()
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)





