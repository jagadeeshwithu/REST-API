from django.db import models

from django.core.validators import RegexValidator


class Employee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?[0-9]+?\d{9,15}$', message="Phone number must be entered in the format: '+9999999999'")
    phoneno = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=120, blank=True, null=True, unique=True)
    role = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
