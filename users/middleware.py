from django.utils.functional import SimpleLazyObject
from functools import partial
from django.contrib.auth.models import AnonymousUser

def check_funcionario_permission(user):
    return user.groups.filter(name="Funcionário").exists()

class FuncionarioMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.pode_cadastrar = SimpleLazyObject(partial(check_funcionario_permission, request.user))
        response = self.get_response(request)
        return response