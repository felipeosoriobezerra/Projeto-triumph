from django.contrib.auth.mixins import UserPassesTestMixin


class FuncionarioPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Funcionário"):
            return True
        return False