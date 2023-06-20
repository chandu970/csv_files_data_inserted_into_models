from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import csv
from app.models import *
def bank(request):
    f='C:\\Users\\91630\\OneDrive\\Desktop\\django\\peter\\Scripts\\csfiles\\bank.csv'
    with open(f,'r') as file:
        csv_data=csv.reader(file)

        next(csv_data)

        for row in csv_data:
            bn=row[0].strip()
            b_n=Banks(bank_name=bn)
            b_n.save()

        return HttpResponse('successful!!!')

def branch(request):
    f='C:\\Users\\91630\\OneDrive\\Desktop\\django\\peter\\Scripts\\csfiles\\branch1.csv'
    with open(f,'r') as file:
        csv_data=csv.reader(file)

        next(csv_data)

        for row in csv_data:
            brn=row[0]
            bro=Banks.objects.get(bank_name=brn)

            instance=Branches(
                bank_name=bro,
                IFSC=row[1],
                branch_name=row[2],
                address=row[3],
                contact=row[4],
                city=row[5],
                district=row[6],
                state=row[7],

            )
            instance.save()
        return HttpResponse('successful!@!')











