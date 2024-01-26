from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255, verbose_name = 'kategory nomi')

    def  __str__(self):
        return self.name
    
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255, verbose_name='post title')
    content = models.TextField(verbose_name='post kontenti')
    image = models.ImageField(upload_to='post-image/')
    date = models.DateTimeField(auto_now=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)



    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})
    
