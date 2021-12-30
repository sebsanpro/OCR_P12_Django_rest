from django.contrib.auth import password_validation
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext, gettext_lazy as _


class EpicUser(AbstractUser):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None
        self.groups.clear()
        Group.objects.get(name=self.team).user_set.add(self)

    phone = PhoneNumberField(unique=True,
                             null=True,
                             blank=True,
                             verbose_name=_('Phone'))

    class Team(models.TextChoices):
        Manager = 'MNG', _('Manager')
        Vendor = 'VDR', _('Vendor')
        Support = 'SUP', _('Support')

    team = models.CharField(max_length=3,
                            choices=Team.choices,
                            verbose_name=_('Team'),
                            blank=False,
                            null=False,
                            default=Team.Manager)

    def is_manager(self):
        return self.groups.filter(name='MNG').exists()

    def is_vendor(self):
        return self.groups.filter(name='VDR').exists()

    def is_support(self):
        return self.groups.filter(name='SUP').exists()

    class Meta:
        ordering = ['last_name']
        verbose_name = _('User')
        verbose_name_plural = _('Users')
