from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='index'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/', views.post_detail, name='post_detail'),
    path('contact-us/', views.contact_us, name='contact-us'),
    #harchi ke bade åath bezani ba / un mishe adresi ke mikhay
]
