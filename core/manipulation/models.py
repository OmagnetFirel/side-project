from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'images'