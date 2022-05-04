from django.db import models

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=50, null=False)
    image = models.ImageField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.id}, {self.name}'
