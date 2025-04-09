from django.db import models

# Create your models here.
from django.db import models

class Webinar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Workshop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.CharField(max_length=100, choices=[("Beginner", "Beginner"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced")])
    price = models.DecimalField(max_digits=8, decimal_places=2)
    schedule = models.DateField()

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    duration = models.CharField(max_length=50)  # e.g., "6 weeks"
    price = models.DecimalField(max_digits=8, decimal_places=2)
    certificate = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class DFYTool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)  # e.g., "Chatbot", "Dashboard"
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='dfy_tools/', null=True, blank=True)

    def __str__(self):
        return self.name


class RetainerPlan(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    monthly_fee = models.DecimalField(max_digits=8, decimal_places=2)
    benefits = models.TextField()

    def __str__(self):
        return self.name


class AcceleratorPackage(models.Model):
    name = models.CharField(max_length=100)
    features = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.name
