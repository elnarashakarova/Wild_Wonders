# Create your models here.

from django.db import models
from django.conf import settings
from django.utils import timezone

import textwrap

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    excerpt = models.TextField(blank=True, null=True)  # field for the highlight
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    
    def get_excerpt(self):
    # Return the provided excerpt or generate one from the text
        if self.excerpt:
            return self.excerpt
        else:
            # Create an excerpt by taking the first 3 sentences from the text
            return ' '.join(textwrap.wrap(self.text, width=200)[:2]) + '...'
    