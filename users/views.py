from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages import views
from django.utils.translation import gettext_lazy as _
from django.views.generic import *
from django.views import generic
from django.contrib.auth.models import Group
from users.permissions import *
from django.views import View
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib.auth.mixins import AccessMixin

class SuperuserRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

User = get_user_model()

class UserDetailView(DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(SuperuserRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user

user_update_view = UserUpdateView.as_view()

class UserRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

class UsersListView(SuperuserRequiredMixin, generic.ListView):
    model = User
    ordering = ["name"]
    template_name = "lista_users.html"

class UserDeleteView(SuperuserRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("users:lista_usuarios")
    success_message = "reserva cancelada com sucesso!!"

    def test_func(self):
        return self.request.user.groups.filter(name="Funcionário").exists()

class RemoveGrupoFuncionarioView(SuperuserRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['pk'])
        grupo_funcionario = Group.objects.get(name='Funcionário')
        user.groups.remove(grupo_funcionario)

        return HttpResponseRedirect(reverse('users:lista_usuarios'))
    
class AtualizarGrupoFuncionarioView(SuperuserRequiredMixin, LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['pk'])
        grupo_funcionario = Group.objects.get(name='Funcionário')
        user.groups.add(grupo_funcionario)

        return HttpResponseRedirect(reverse('users:lista_usuarios'))

class UserCreateView(SuperuserRequiredMixin, views.SuccessMessageMixin, CreateView):
    model = User
    form_class = UserSignupForm
    success_url = reverse_lazy("users:list")
    success_message = _("Usuário cadastrado com sucesso!")
    template_name = "account/signup.html"