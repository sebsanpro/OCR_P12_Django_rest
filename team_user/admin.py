from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from team_user.models import EpicUser
from django.utils.translation import gettext, gettext_lazy as _


@admin.register(EpicUser)
class EpicUserAdmin(UserAdmin):
    model = EpicUser

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'team'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
