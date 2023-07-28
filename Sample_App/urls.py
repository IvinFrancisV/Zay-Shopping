from django.urls import path
from Sample_App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_about/',views.view_about, name='view_about')
]