from django.contrib import admin
from django.urls import path, include
from conectaplusapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projetos'),
    path('projetos/projetoX', views.projetoX, name='projetoX'),
    path('projetos/projetoY', views.projetoY, name='projetoY'),
    path('projetos/projetoW', views.projetoW, name='projetoW'),
    path('projetos/projetoZ', views.projetoZ, name='projetoZ'),
    path('caçadores/', views.cacadores, name='caçadores'),
    path('inicio/', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('voluntarios/', views.voluntarios, name='voluntarios'),
    path('chat_geral/', views.chat_geral, name='chat_geral'),
    path('login/', views.login_user, name = 'login'),
    path('send_message/', views.send_message, name='send_message'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]