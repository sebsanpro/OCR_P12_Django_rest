from django.contrib import admin

from client.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company', 'last_name', 'email', 'phone', 'sale_contact', 'prospect')
    search_fields = ('company', 'last_name', 'email', 'phone', 'sale_contact', 'prospect')
    list_filter = ('sale_contact', 'prospect')
