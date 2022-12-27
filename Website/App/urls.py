from django.urls import path

from . import views 

urlpatterns = [
    path('',views.index, name='index'),
    path('AboutWe',views.aboutwe, name='aboutwe'),
    path('Project',views.project, name='project'),
]