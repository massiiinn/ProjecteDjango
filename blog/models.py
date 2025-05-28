from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(max_length=300)
    image_name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(unique=True, blank=False)
    content = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField('Tag')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag

