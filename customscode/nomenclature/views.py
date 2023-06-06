from django.shortcuts import render
from django.http import HttpResponse
   
def nomenclature(request):
    return render(request, 'nomenclature.html')
