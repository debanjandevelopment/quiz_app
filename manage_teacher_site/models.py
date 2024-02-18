from django.db import models

# Create your models here.
class CreateQuestionPaper(models.Model):
    class SubjectList(models.TextChoices):
        MATH = "Math","Math"
        ENGLISH = "English","English"
        OTHER = "Other","Other"
    question_paper_name = models.CharField(max_length=250)
    total_question = models.IntegerField()
    exam_time = models.IntegerField()
    subject = models.CharField(choices=SubjectList.choices,max_length=50,default=SubjectList.OTHER)