from django.db import models

# Create your models here.
from django.db import models

class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    featured_image = models.ImageField(upload_to='industries/', blank=True, null=True)
    use_cases = models.TextField(help_text="Explain how AI helps this industry.")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
