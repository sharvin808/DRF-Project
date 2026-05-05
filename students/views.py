from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    students = [
        {'id':1, 'name': 'John Locke', 'age':60}
    ]
    return HttpResponse(students)
