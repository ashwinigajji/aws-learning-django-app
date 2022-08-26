from django.db import models

# Create your models here.
from django.db import models

class Note(models.Model):
    title = models.TextField()
    description = models.TextField()
    end_date = models.DateField()
    Attachment = models.FileField(upload_to='media', default='settings.MEDIA_ROOT/media/test.txt')