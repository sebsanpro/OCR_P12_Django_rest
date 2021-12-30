from django.conf import settings
from django.db import models
from django.utils.translation import gettext, gettext_lazy as _

from client.models import Client


class Contract(models.Model):
    sale_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     verbose_name=_('Sale Contact'),
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     limit_choices_to={'groups__name': 'VDR'})
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE)
    date_create = models.DateTimeField(_('Creation date'), auto_now_add=True)
    date_update = models.DateTimeField(_('Last update'), auto_now=True)
    status = models.BooleanField(_('Contract signed'), default=False)
    amount = models.FloatField(_('Amount'))
    payment_due_date = models.DateTimeField(_('Payment due date'))

    def __str__(self):
        if self.status:
            return '%s %s %s' % (self.client, self.sale_contact, _('signed'))
        else:
            return '%s %s %s' % (self.client, self.sale_contact, _('in progress'))

    class Meta:
        ordering = ['client']
        verbose_name = _('Contract')
        verbose_name_plural = _('Contracts')
