from django.urls import path
from users.views import *
from . import views

app_name = "users"

urlpatterns = [
    path("redirect/", view=user_redirect_view, name="redirect"),
    path("update/", view=user_update_view, name="update"),
    path('detalhe_user/<int:pk>/', User2DetailView.as_view(), name='detalhe_user'),
    path('lista_users/', views.UsersListView.as_view(), name='lista_usuarios'),
    path('create_users/', views.UserCreateView.as_view(), name='create_users'),
    path('delete_users/<int:pk>/', views.UserDeleteView.as_view(), name='delete_users'),
    path('atualizar-grupo-funcionario/<int:pk>/', views.AtualizarGrupoFuncionarioView.as_view(), name='atualizar_grupo_funcionario'),
    path('remover-grupo-funcionario/<int:pk>/', views.RemoveGrupoFuncionarioView.as_view(), name='remover_grupo_funcionario'),

]