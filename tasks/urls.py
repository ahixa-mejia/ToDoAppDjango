from django.urls import path
from . import views
from .views import registrar_usuario

urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('login/', views.ingresar, name="ingresar"),
    path('registrar/', registrar_usuario, name='registrar_usuario'),

  ]