# Generated by Django 4.2.6 on 2023-11-14 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('sended',)},
        ),
    ]
