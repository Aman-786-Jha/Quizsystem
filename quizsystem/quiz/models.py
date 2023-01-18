from django.db import models

# Create your models here.

class Quiz(models.Model):
    id= models.TextField(primary_key=True)
    questions = models.TextField()
    answers= models.IntegerField(blank=False,null=True)
    option1 = models.TextField(blank=True)
    option2 = models.TextField(blank=True)
    option3 = models.TextField(blank=True)
    option4 = models.TextField(blank=True)

    def __str__(self):
        return self.questions + 'correct_option' + str(self.answers)

