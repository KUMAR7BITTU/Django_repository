from django.http import HttpResponse # This will give the response on browser .
from django.shortcuts import render

def Home(request):
    data = {
        "title" : "Home New",
        "bdata" : "Welcome to PARADIP",
        "clist" : ['PHP', 'JAVA', 'DJANGO'],
        "student_details" : [
            {'name' : 'pradeep', 'phone' : 8018830741},
            {'name' : 'manoj', 'phone' : 9937873511}
        ]
        }
    return render(request,"index.html",data)

def home(request):
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

def homepage(request):
    return HttpResponse("<b>Welcome to homepage </b>")

def courseInt2(request,course_id2):
    return HttpResponse(course_id2)

def courseStr2(request,statement3):
    return HttpResponse(statement3)

def courseSlug2(request,statement4):
    return HttpResponse(statement4)

def course_data2(request,statement):
    return HttpResponse(statement)