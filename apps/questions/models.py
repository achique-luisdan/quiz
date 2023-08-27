from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class Topic (models.Model):
    ordinal = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=120, null=False, blank=False)
    icon = models.CharField(max_length=355, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Question (models.Model):
    code = models.UUIDField(default=uuid4, unique=True, null=False)
    text = models.TextField(null=False)
    points = models.IntegerField(null=False, default=0)
    correct_comment  = models.CharField(max_length=120, null=True)
    incorrect_comment  = models.CharField(max_length=120, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, related_name='questions')
    # Una pregunta tiene mínimo 2, máximo 3 opciones.

    def __str__(self):
        return self.text


class Option (models.Model):
    text = models.TextField(null=False)
    snippet =  models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False,  null=False)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, related_name='options')
    # Una pregunta puede tener de 1 a 3 opciones correctas.

    def __str__(self):
        return self.text


class Answer (models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    select = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, related_name='answers')
    created_date  = models.DateTimeField(auto_now_add=True)