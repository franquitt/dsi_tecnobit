# Generated by Django 2.0.13 on 2019-06-12 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criticidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'criticidad',
                'verbose_name_plural': 'criticidades',
            },
        ),
    ]