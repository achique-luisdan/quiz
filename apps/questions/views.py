from rest_framework import viewsets
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Topic, Question, Option, Answer

from .serializers import TopicSer, QuestionSer, OptionSer, AnswerSer, UserSer


class TopicView(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSer

    def create(self, request, *args, **kwargs):
        serializer = TopicSer(data=request.data,  many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSer


class OptionView(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSer


class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)