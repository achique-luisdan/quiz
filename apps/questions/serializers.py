from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Topic, Question, Option, Answer

class TopicSer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


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



class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user