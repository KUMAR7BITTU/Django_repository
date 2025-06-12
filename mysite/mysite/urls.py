"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views # Here mysite is our app and view is file .

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('about-us/',views.aboutus),
    path('course/',views.course),
    path('courseInt/<int:course_id>',views.courseInt),
    path('courseStr/<str:statement1>',views.courseStr),
    path('courseSlug/<slug:statement2>',views.courseSlug),
    path('course_data/<item>',views.course_data),
    path('',views.Home),
    path('homepage/',views.homepage),
    path('courseInt2/<int:course_id2>',views.courseInt2),
    path('courseStr2/<str:statement3>',views.courseStr2),
    path('courseSlug2/<slug:statement4>',views.courseSlug2),
    path('course_data2/<statement>',views.course_data2)
]

# site is class and urls is a function in site class .
