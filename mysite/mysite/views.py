from django.http import HttpResponse

def aboutus(request):
    return HttpResponse(" <b> Welcome to my site </b>")

def course(request):
    return HttpResponse("Welcome to our course")