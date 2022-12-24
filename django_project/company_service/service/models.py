from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=16, verbose_name='Name')
    lastname = models.CharField(max_length=26, verbose_name='Last name')
    email = models.EmailField(verbose_name='Email')
    phone = models.IntegerField(verbose_name='Phone')

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = ['lastname']


class Companies(models.Model):
    name = models.CharField(max_length=16, verbose_name='Name')
    houses = models.ForeignKey('Houses', on_delete=models.PROTECT, verbose_name='Houses list')

    class Meta:
        verbose_name_plural = 'Companies'
        verbose_name = 'Companie'
        ordering = ['name']


class Houses(models.Model):
    city = models.TextField(verbose_name='City')
    street = models.TextField(verbose_name='Street')
    number_house = models.IntegerField(verbose_name='Number house')

    class Meta:
        verbose_name_plural = 'Houses'
        verbose_name = 'House'
        ordering = ['city']
