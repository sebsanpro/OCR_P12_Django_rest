from django.contrib import admin

from event.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('client', 'contract', 'support_contact', 'status', 'event_date')
    list_filter = ('support_contact', 'status')
    search_fields = ('client', 'contract', 'support_contact', 'status', 'event_date')
