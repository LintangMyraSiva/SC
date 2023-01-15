from django.urls import path

from . import views 

urlpatterns = [
    path('',views.index, name='index'),
    path('AboutUs',views.aboutus, name='aboutus'),
    path('Project',views.project, name='project'),
]