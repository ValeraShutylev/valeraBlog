from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    slug = models.SlugField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    link = models.URLField(blank=True)
    link_description = models.CharField(max_length=140, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('getpost', args=[self.slug])
