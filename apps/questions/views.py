from rest_framework import viewsets

from .models import Question, Option, Answer
from .serializers import QuestionSer, OptionSer, AnswerSer

class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSer


class OptionView(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSer


class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSer