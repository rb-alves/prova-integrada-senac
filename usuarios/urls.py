from django.urls import path
from usuarios import views

urlpatterns = [
    path("usuarios/", views.listaUsuarios, name="lista_usuarios"),
    path("novoUsuario/", views.novoUsuario, name="novo_usuario"),
]
