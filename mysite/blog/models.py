from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    # 定义类似objects管理类，以便API可以直接调用如Post.published.all()，不用再用默认的管理类Post.objects.all()
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    objects = models.Manager()                      # 这里是默认的管理类名字
    published = PublishedManager()                  # 这里指定是调用时的名字，如Post.published.all()中的名字
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='dratf')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
