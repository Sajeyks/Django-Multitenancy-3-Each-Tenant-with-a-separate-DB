from django.db import models
from django.core.validators import RegexValidator

subdomain_validator = RegexValidator(
    r'^[a-zA-Z0-9-]+$',
    'Enter a valid subdomain name.'
)

class Tenant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subdomain_prefix = models.CharField(max_length=100, unique=True, validators=[subdomain_validator])
    
    @property
    def db_name(self):
        return "database_"+str(self.id)
    
    def __str__(self):
        return self.name

class customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    
CHOICES_1 = (
        ("development", 'Development'),
        ("integration", 'Integration'),
        ("testing", 'Testing'),
        ("ready", 'Ready'),
        ("maintainance", 'Maintainance'),
    )

class rocket(models.Model):
    name = models.CharField(max_length=255, unique=True)
    edition = models.CharField(max_length=255)
    stage = models.CharField(max_length=255, choices=CHOICES_1)
    build_start = models.DateTimeField()
    build_end = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
CHOICES_2 = (
        ("launched", 'Launched'),
        ("postponed", 'Postponed'),
        ("ready", 'Ready'),
        ("failed", 'Failed'),
    )

class launch(models.Model):
    rockets = models.ManyToManyField(rocket, blank=True)
    launch_time = models.DateTimeField()
    status = models.CharField(max_length=255, choices=CHOICES_2)
    
    class  Meta:
        verbose_name_plural  =  "Launches"

class payload(models.Model):
    name = models.CharField(max_length=255, unique=True)
    weight = models.FloatField(help_text="in Tonnes")
    owner = models.ForeignKey(customer, on_delete = models.CASCADE)
    rocket = models.ForeignKey(rocket, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name