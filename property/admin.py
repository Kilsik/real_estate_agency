from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year',
        'town', 'owners_phonenumber', 'owner_pure_phone']
    list_editable = ['new_building',]
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by',]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 3


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats',]
    list_display = ['full_name', 'pure_phone']
    search_fields = ['full_name', 'pure_phone']
    inlines = [OwnerInline]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)