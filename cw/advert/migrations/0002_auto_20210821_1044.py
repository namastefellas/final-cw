# Generated by Django 3.2.6 on 2021-08-21 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'permissions': [('moderate', 'Moderated user or not')], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelTable(
            name='advert',
            table='adverts',
        ),
    ]
