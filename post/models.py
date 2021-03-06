from django.db import models
from django.utils.timezone import now

# Create your models here.
class PostQuerySet(models.QuerySet):
    def rank_1(self):
        return self.filter(rating='5')


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model,using=self._db)

    def rank_1(self):
        return self.get_queryset().rank_1()


    # def rank_1(self):
    #     return self.get_queryset().rank_1()

class Category(models.Model):
    category=models.CharField(max_length=50)
    rating=models.IntegerField(default=0)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return self.category

class Post(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=500,blank=True)
    post = models.TextField(blank=True)
    post_para_2 = models.TextField(blank=True)
    post_para_3 = models.TextField(blank=True)
    captions=models.TextField(blank=True)
    captions_para_2 = models.TextField(blank=True)
    captions_para_3 = models.TextField(blank=True)
    quote=models.CharField(max_length=200,blank=True)
    quote_by=models.CharField(max_length=100,blank=True)
    image=models.ImageField(upload_to='post_image/%Y/%m/%d/',blank=True)
    date= models.DateTimeField(default=now)
    related_post_1 = models.CharField(max_length=100,blank=True)
    related_link_1 = models.CharField(max_length=100,blank=True)
    related_post_2 = models.CharField(max_length=100,blank=True)
    related_link_2 = models.CharField(max_length=100,blank=True)
    related_post_3 = models.CharField(max_length=100,blank=True)
    related_link_3 = models.CharField(max_length=100,blank=True)
    rating=models.IntegerField(default=0)


    objects=PostManager()

    def __str__(self):
        return self.title


