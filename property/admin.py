from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner','flat']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year',
        'town', 'display_pure_phone']
    list_editable = ['new_building',]
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by',]
    inlines = [FlatInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats',]
    list_display = ['full_name', 'pure_phone']
    search_fields = ['full_name', 'pure_phone', 'phonenumber']
    inlines = [FlatInline]

