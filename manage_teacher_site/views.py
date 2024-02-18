from django.shortcuts import render,redirect


def dashboard(request):
    return render (request,'dashboard.html')

def add_exam(request):
    return render(request,'create_exam.html')