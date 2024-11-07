from django.urls import path
from collo_app import views

urlpatterns=[
    path('',views.index,name="My_index"),
    path('about/',views.about,name="My_about"),
    path('blog/',views.blog,name="My_blog"),
    path('contact/',views.contact,name="My_contact"),
    path('services/',views.services,name="My_services"),
    path('another/',views.another,name="My_another"),



]