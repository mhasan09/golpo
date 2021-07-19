from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    avatar = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.user.username

User.UserProfile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class POST(models.Model):
    body = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='oinks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.body


class Like(models.Model):
    post = models.ForeignKey(POST, related_name='likes', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
