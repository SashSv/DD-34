from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    test_for_me = models.TextField()

    def __str__(self):
        return f'{self.title} : {self.description}'

    def get_absolute_url(self):
        return f'/news/{self.id}'