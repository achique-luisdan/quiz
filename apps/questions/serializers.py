from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Topic, Question, Option, Answer

class OptionSer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'snippet']

class QuestionSer(serializers.ModelSerializer):
    options = OptionSer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'code', 'text', 'points', 'options']

class TopicSer(serializers.ModelSerializer):
    questions = QuestionSer(many=True, read_only=True)
    class Meta:
        model = Topic
        fields = '__all__'




class QuestionToSer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['correct_comment', 'incorrect_comment']

class OptionToSer(serializers.ModelSerializer):
    question = QuestionToSer(read_only=True)
    class Meta:
        model = Option
        fields =  '__all__'


class AnswerSer(serializers.ModelSerializer):
    select = OptionToSer(read_only=False)
    class Meta:
        model = Answer
        fields = '__all__'



class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user