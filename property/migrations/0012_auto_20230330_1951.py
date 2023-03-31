# Generated by Django 3.2.18 on 2023-03-30 16:51

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20230330_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_complaints', to='property.flat', verbose_name='Квартира, на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='address',
            field=models.TextField(db_index=True, help_text='ул. Подольских курсантов д.5 кв.4', verbose_name='Адрес квартиры'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='town_district',
            field=models.CharField(blank=True, db_index=True, help_text='Чертаново Южное', max_length=50, verbose_name='Район города, где находится квартира'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(null=True, related_name='related_owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]