# Generated by Django 2.2.24 on 2023-03-29 12:46

from django.db import migrations


def set_new_building(apps, schema_editor):
    '''
    Setting the value of the field Flat.new_building
    '''
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year>=2015).update(new_building = True)
    Flat.objects.filter(construction_year<2015).update(new_building = False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(set_new_building)
    ]
