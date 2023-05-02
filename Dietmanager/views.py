from django.shortcuts import render


def index(request):
    return render(request, 'main.html')

def  callorylist(request):
    return render(request, 'callorylist.html')


def  callorycalculator(request):
    return render(request, 'callorycalculator.html')