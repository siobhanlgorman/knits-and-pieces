from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=True)
    email_address = models.EmailField(max_length=500, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return f'{ self.name }'
