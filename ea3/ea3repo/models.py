from django.db import models

class Level(models.Model):
    GOALS_INITIATIVES = 'Goals & Initiatives'
    PRODUCTS_SERVICES = 'Products & Services'
    DATA_INFORMATION = 'Data & Information'
    SYSTEMS_APPLICATION = 'Systems & Application'
    NETWORKS_INFRASTRUCTURE = 'Networks & Infrastructure'
    LEVEL_CHOICES = [
        (GOALS_INITIATIVES, 'Goals & Initiatives'),
        (PRODUCTS_SERVICES, 'Products & Services'),
        (DATA_INFORMATION, 'Data & Information'),
        (SYSTEMS_APPLICATION, 'Systems & Application'),
        (NETWORKS_INFRASTRUCTURE, 'Networks & Infrastructure')
    ]
    
    name = models.CharField(max_length=30, choices=LEVEL_CHOICES, default=GOALS_INITIATIVES)

    def __str__(self):
        return self.name


class Artifact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default=Level.GOALS_INITIATIVES)
    quantity = models.IntegerField(default=1)
    use_frequency = models.CharField(max_length=20, choices=(
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ), default='low')
    
    def __str__(self):
        return self.name