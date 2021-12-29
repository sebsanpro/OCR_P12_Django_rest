from django.contrib import admin

from contract.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'sale_contact', 'status', 'amount', 'payment_due_date')
    search_fields = ('client', 'sale_contact', 'status', 'amount', 'payment_due_date')
    list_filter = ('status', 'sale_contact')
