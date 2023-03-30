# Generated by Django 3.2.18 on 2023-03-30 09:53

from django.db import migrations


def trasfer_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats:
        owner = flat.owner
        owners_phonenumber = flat.owners_phonenumber
        owner_pure_phone = flat.owner_pure_phone
        Owner.objects.get_or_create(full_name=owner,
            pure_phone=owner_pure_phone, defaults={
            'phonenumber': owners_phonenumber
            })


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
    migrations.RunPython(trasfer_owners)
    ]
