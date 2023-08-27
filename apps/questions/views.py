from rest_framework import viewsets
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
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

    def get_queryset(self):
        # Reverse ForeignKey relationship
        topics = Topic.objects.prefetch_related('questions').all()
        return topics

class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSer


class OptionView(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSer


class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSer

    def list(self, request):
        return Response({
                            'error': 'Unauthorized',
                            'description': 'It is not allowed to see the answers of other users.'},
                         status=HTTP_401_UNAUTHORIZED
                        )
    def retrieve(self, request, pk=None):
        return Response({
                            'error': 'Unauthorized',
                            'description': 'It is not allowed to see the answers of other users.'},
                         status=HTTP_401_UNAUTHORIZED
                        )


    def update(self, request, pk=None):
        return Response({
                            'error': 'Unauthorized',
                            'description': 'After you submit your answer, you cannot edit it.'},
                         status=HTTP_401_UNAUTHORIZED
                        )
    def destroy(self, request, pk=None):
        return Response({
                            'error': 'Unauthorized',
                            'description': 'Submitted responses cannot be deleted.'},
                         status=HTTP_401_UNAUTHORIZED
                        )

    def get_queryset(self):
        # Reverse ForeignKey relationship
        answers = Answer.objects.prefetch_related('select').all()
        return answers

    def create(self, request,  *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            answer = serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            select = serializer.data['select']
            user = serializer.data['user']
            option = Option.objects.get(id = select)
            other_serializer = self.serializer_class(data={ 'select': OptionSer (option).data, 'user': user})
            if other_serializer.is_valid(raise_exception=True):
                answer = Answer.objects.create()
                if user != None:
                    userObject = User.objects.get(id=1)
                answer.user = userObject
                answer.select = option
                answer.save()
                return Response(AnswerSer(answer).data, status=HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


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