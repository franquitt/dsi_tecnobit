# Generated by Django 2.0.13 on 2019-06-12 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polocApp', '0003_auto_20190612_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudmantenimiento',
            name='fechaCreacion',
        ),
    ]
