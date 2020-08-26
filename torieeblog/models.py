from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
# Create your models here.


class Genres(models.TextChoices):
    POLITICAL_NEWS = "political_news"
    FICTION = "fiction"
    SPORTS = "sports"
    MUSIC = "music"
    ART = "art"
    FASHION = "fashion"
    MOVIES = "movies"
    SCIENCE = "science"
    HEALTH = "health"


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(
        max_length=50, choices=Genres.choices, default=Genres.POLITICAL_NEWS)
    thumbnail = models.URLField(max_length=200, null=True)
    excerpt = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    read_time = models.CharField(max_length=10, default="10-mins")
    featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug

        while(queryset):
            slug = original_slug + "-" + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = BlogPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass

        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
