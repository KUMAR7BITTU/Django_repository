from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,"index.html")

def aboutus(request):
    return HttpResponse(" <b> Welcome to my site </b>")

def course(request):
    return HttpResponse("Welcome to our course")

def courseInt(request,course_id):
    return HttpResponse(course_id)

def courseStr(request,statement1):
    return HttpResponse(statement1)

def courseSlug(request,statement2):
    return HttpResponse(statement2)

def course_data(request,item):
    return HttpResponse(item)