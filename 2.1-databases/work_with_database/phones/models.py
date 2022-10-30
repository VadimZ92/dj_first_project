from django.db import models

class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.URLField(max_length=200)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'

    # def get_url(self):
    #     return reverse("phone", kwargs={"slug": self.slug})