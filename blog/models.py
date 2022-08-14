from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="blog/images/")
    created_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title