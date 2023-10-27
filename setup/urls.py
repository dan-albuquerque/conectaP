from django.contrib import admin
from django.urls import path, include
from conectaplusapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projetos'),
    path('caçadores/', views.cacadores, name='caçadores'),
    path('inicio/', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('voluntarios/', views.voluntarios, name='voluntarios'),
    path('chat_geral/', views.chat_geral, name='chat_geral'),
]