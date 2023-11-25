from django.contrib.auth.mixins import UserPassesTestMixin

class FuncionarioPermission(UserPassesTestMixin):
    def is_funcionario(user):
        return user.groups.filter(name='Funcionário').exists()