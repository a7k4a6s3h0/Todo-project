from django.db import models
from django.utils.text import slugify
# Create your models here.


class User_Tasks(models.Model):

    task_name = models.CharField(max_length=50, null=False)
    task_describtion = models.CharField(max_length=500, null=False)
    created_at = models.DateField()
    updated_at = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)
    

    def __str__(self) -> str:
        return self.task_name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.task_name)
        return super(User_Tasks, self).save(*args, **kwargs)