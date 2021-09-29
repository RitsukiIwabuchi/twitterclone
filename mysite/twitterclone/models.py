from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    favorites = models.ManyToManyField(User, related_name="favorites")

    def __str__(self):
        return self.tweet

    def get_absolute_url(self):
        return reverse("twitterclone:my-tweets", kwargs={"username": self.user.username})

    class Meta:
        ordering = ["-created_at"]

class Follow(models.Model):
    follow_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow_user")
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed_user")
    followed_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["follow_user", "followed_user"],
                name="following_unique"
            ),
        ]