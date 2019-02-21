from django.db import models
from django.utils import timezone


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '%s %s' % (self.title, self.pub_date)


class Posts(models.Model):
    blogs = models.OneToOneField(Blogs, on_delete=models.CASCADE, related_name='posts')
    post_text = models.TextField()
    bloger = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
