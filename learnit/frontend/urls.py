from django.urls import path
from frontend import views
from django.contrib.auth import views as auth_views



app_name = 'frontend'
urlpatterns = [  
 path('', views.index, name='index'),
 path('about-page', views.about, name='about'),
 path('contact-page/', views.contact, name='contact'),
 path('course-page', views.courses, name='courses'),
 path('course-details', views.course_details, name='course-details'),
 path('element-page', views.elements, name='elements'),
 
] 