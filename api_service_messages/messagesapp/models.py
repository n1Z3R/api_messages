from django.db import models


class MessageModel(models.Model):
    REVIEW = "r"
    BLOCKED = "b"
    CORRECT = "c"
    CHOICES = (
        (REVIEW, "review"),
        (BLOCKED, "blocked"),
        (CORRECT, "correct"),
    )

    user_id = models.IntegerField()
    message = models.CharField(max_length=200)
    status = models.CharField(choices=CHOICES, default=REVIEW, max_length=50)

    def __str__(self):
        return self.message
