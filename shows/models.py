from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 5:
            errors['title'] = 'Show title must be at least 5 charcters'
        if len(postData['description']) < 10:
            errors['description'] = 'Show description must be at least 10 chatacters'
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    network = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __str__(self):
        return f'title: {self.title}'



# Create your models here.
