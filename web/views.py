from django.shortcuts import render
from django.http import HttpResponse

def styles(request):
    return render(request, 'styles.html')
