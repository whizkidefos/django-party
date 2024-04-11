import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass


class Party(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    party_date = models.DateField()
    party_time = models.TimeField()
    invitation = models.TextField()
    venue = models.CharField(max_length=255)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_parties')
    
    class Meta:
        verbose_name_plural = 'Parties'

    def __str__(self):
        return f"{self.venue}, {self.party_date}, {self.party_time}"


class Gift(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gift = models.CharField(max_length=255)
    price = models.FloatField(blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.gift
    

class Guest(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    attending = models.BooleanField(default=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='guests')
    
    
    def __str__(self):
        return str(self.name)