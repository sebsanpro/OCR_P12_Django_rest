from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext, gettext_lazy as _


class Client(models.Model):
    company = models.CharField(_('Company'), max_length=50)
    first_name = models.CharField(_('First name'), max_length=50)
    last_name = models.CharField(_('Last name'), max_length=50)
    email = models.EmailField(verbose_name=_('Courriel'), max_length=50)
    phone = PhoneNumberField(unique=True, verbose_name=_('Phone'))
    mobile = PhoneNumberField(unique=True, verbose_name=_('Mobile'))
    date_create = models.DateTimeField(_('Creation date'), auto_now_add=True)
    date_update = models.DateTimeField(_('Last update'), auto_now=True)
    sale_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     verbose_name=_('Sale Contact'),
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     limit_choices_to={'groups__name': 'VDR'})
    prospect = models.BooleanField(_('Prospect'), default=True)

    def __str__(self):
        return '%s | %s %s | %s | %s' % (self.company, self.last_name, self.first_name , self.email, self.phone)

    class Meta:
        ordering = ['company']
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
