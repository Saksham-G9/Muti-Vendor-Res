from django.contrib import admin

from vendor.models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'vendor_license', 'created_at')
    search_fields = ('user__username', 'vendor_license')
    list_filter = ('created_at',)

admin.site.register(Vendor, VendorAdmin)