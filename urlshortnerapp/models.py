from django.db import models

class ShortUrl(models.Model):
    shortUrl = models.CharField(max_length=255, blank=True)
    originalUrl = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.originalUrl