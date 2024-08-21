from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.service_page, name='service_page'),
    path('service/<int:pk>/',views.service_detail, name='service_detail'),
    path('projects/', views.projects, name='projects'),
    path('send_email/',views.send_email, name='send_email'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
   
] 
 