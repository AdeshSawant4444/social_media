from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    follows=models.ManyToManyField('self',related_name='followed_by',symmetrical=False,blank=True )
    created_at=models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    profile=models.ForeignKey(Profile,related_name='posts',on_delete=models.CASCADE)
    post=models.TextField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    on_post=models.ForeignKey(Post,on_delete=models.CASCADE)
    by_profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    comment=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        p=Profile(user=instance)
        p.save()
        p.follows.add(p.id)
        p.save()

