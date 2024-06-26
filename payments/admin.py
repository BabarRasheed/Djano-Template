# admin.py

from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('stripe_charge_id', 'amount', 'timestamp', 'status', 'description')
    search_fields = ('stripe_charge_id', 'status')
    list_filter = ('status', 'timestamp')
