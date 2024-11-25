from django.urls import path
from . import views

# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('acceso/', views.acceso, name='acceso'),
    path('menu/', views.menu, name='menu'),
    path('informacion/', views.informacion_del_miembro, name='informacion_del_miembro'),
    path('eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
]
