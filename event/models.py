from django.conf import settings
from django.db import models
from django.utils.translation import gettext, gettext_lazy as _
from client.models import Client
from contract.models import Contract


class Event(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract,
                                 on_delete=models.CASCADE)
    date_create = models.DateTimeField(_('Creation date'), auto_now_add=True)
    date_update = models.DateTimeField(_('Last update'), auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=models.CASCADE)

    class EventStatus(models.TextChoices):
        Created = 'CRE', _('Created')
        Affected = 'AFF', _('Affected')
        Ended = 'END', _('Ended')

    status = models.CharField(_('Event Status'),
                              max_length=3,
                              choices=EventStatus.choices,
                              blank=False,
                              null=False,
                              default=EventStatus.Created)
    attendees = models.PositiveIntegerField(_('Attendees person'), default=1)
    event_date = models.DateTimeField(_('Event date'))
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s | %s | %s | %s | %s' % (self.client, self.contract, self.support_contact,
                                           self.status, self.event_date)

    class Meta:
        ordering = ['client']
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
