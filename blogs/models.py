from django.db import models

class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft')
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('core.CustomUser', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datatime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title

