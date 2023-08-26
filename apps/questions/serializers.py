from rest_framework import serializers

from .models import Question, Option, Answer

class QuestionSer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class OptionSer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class AnswerSer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
