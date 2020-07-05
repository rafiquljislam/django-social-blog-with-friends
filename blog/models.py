from django.db import models
from user.models import Profile

class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=360)
    image = models.ImageField(default='post/default.png',upload_to='post/')
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}--{ self.user }"

    def comment_count(self):
        return self.comment_set.all().count()

    def comment(self):
        return self.comment_set.all()
    
    def like(self):
        return self.like_set.filter(value='like').count()

LIKE_OR_UNLIKE=(
    ('like','like'),
    ('unlike','unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_OR_UNLIKE,max_length=6)
    create = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{ self.post }--{ self.user }--{ self.value }"
    
class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{ self.post }--{ self.user }--{ self.value }"
    
