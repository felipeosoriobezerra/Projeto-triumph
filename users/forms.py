from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model, models
from django.forms import EmailField, ModelChoiceField
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        field_classes = {"email": EmailField}

class UserSignupForm(SignupForm):
    group = ModelChoiceField(
        queryset=models.Group.objects.all(),
        required=True,
        label=_("Grupo de permissões"),
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
    )

    is_active = forms.BooleanField(
        initial=True,
        required=False,
        label=_("Is Active"),
    )

    def save(self, request):
        user = super().save(request)
        user.is_active = self.cleaned_data["is_active"]
        user.groups.remove(*user.groups.all())
        user.groups.add(self.cleaned_data["group"])
        user.save()
        return user
