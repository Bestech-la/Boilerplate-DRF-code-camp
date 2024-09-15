from enum import Enum
from django.db import models
from sorl.thumbnail import ImageField
from sorl.thumbnail import delete
from django_cleanup.signals import cleanup_pre_delete

class Subject(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

class ExamType(Enum):
    MID_TERM = 'Mid-term'
    FINAL = 'Final'
    QUIZ = 'Quiz'
    ASSIGNMENT = 'Assignment'
    @classmethod
    def choices(cls):
        """Get choices for Gender as a list of tuples."""
        return [(choice.value, choice.name.replace("_", " ").title()) for choice in cls]

class Exam(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    examType = models.CharField(
        max_length=255, choices=ExamType.choices(), default=ExamType.FINAL.value
    )
    examDate = models.DateTimeField()
    maxScore = models.DecimalField(max_digits=5, decimal_places=2)
    image = ImageField(
        verbose_name="Image", upload_to="image/exam", blank=True, null=True
    )
def sorl_delete(**kwargs):
    delete(kwargs["file"])

cleanup_pre_delete.connect(sorl_delete)
