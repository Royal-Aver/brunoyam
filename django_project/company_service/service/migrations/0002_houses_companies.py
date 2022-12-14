# Generated by Django 4.1.3 on 2022-12-24 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField(verbose_name='City')),
                ('street', models.TextField(verbose_name='Street')),
                ('number_house', models.IntegerField(verbose_name='Number house')),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Name')),
                ('houses', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.houses', verbose_name='Houses list')),
            ],
        ),
    ]
