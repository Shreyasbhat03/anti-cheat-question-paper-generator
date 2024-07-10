from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    speed = models.FloatField()
    duration = models.FloatField()

    def __str__(self):
        return self.question_text
