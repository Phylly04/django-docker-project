from django.db import models
from django.contrib.auth.models import User
# from . import views

# Create your models here.
class User(models.Model):
    """
    Represents a user entity.

    Fields:
    - name (str): The name of the user (maximum length: 15 characters).
    - age (int): The age of the user.
    - email (str): The email address of the user.
    - password (str): The password of the user (maximum length: 15 characters).
    """
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=15)


class SugarIntake(models.Model):
    """
    Represents a user's sugar intake record.

    Fields:
    - user (User): The user associated with the sugar intake record.
    - teaspoons (int): The amount of sugar intake in teaspoons.
    - date (date): The date when the sugar intake record was created (auto-generated).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teaspoons = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class HealthCondition(models.Model):
    """
    Represents a user's health condition.

    Fields:
    - user (User): The user associated with the health condition record.
    - condition (str): The description of the health condition (maximum length: 100 characters).
    - date_diagnosed (date): The date when the health condition was diagnosed.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    date_diagnosed = models.DateField()


class Quiz(models.Model):
    """
    Represents a quiz.

    Fields:
    - user (User): The user who took the quiz.
    - score (int): The score obtained in the quiz.
    - date (datetime): The date and time when the quiz was taken (auto-generated).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    """
    Represents a question in a quiz.

    Fields:
    - text (str): The text of the question (maximum length: 255 characters).
    """
    text = models.CharField(max_length=255)


class Answer(models.Model):
    """
    Represents an answer to a question in a quiz.

    Fields:
    - question (Question): The question associated with the answer.
    - text (str): The text of the answer (maximum length: 255 characters).
    - is_correct (bool): Indicates if the answer is correct or not (default: False).
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)


class UserAnswer(models.Model):
    """
    Represents a user's answer to a question in a quiz.

    Fields:
    - quiz (Quiz): The quiz associated with the user's answer.
    - question (Question): The question to which the user provided the answer.
    - answer (Answer): The answer chosen by the user.
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Comment(models.Model):
    """
    Represents a comment on a quiz.

    Fields:
    - quiz (Quiz): The quiz associated with the comment.
    - user (User): The user who made the comment.
    - text (str): The text of the comment.
    - date (datetime): The date and time when the comment was made (auto-generated).
    """
