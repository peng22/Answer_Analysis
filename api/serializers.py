from rest_framework import serializers
from .models import Responder,Question,Answer


class ResponderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Responder
        fields=['id','name','phone_number','address',
                'DOB','nationality','gender','answered_questions']


class AnswerSerializer(serializers.ModelSerializer):
    responders=ResponderSerializer(many=True, read_only=True)
    class Meta:
        model=Answer
        fields=['id','choice','responders']

class QuestionSerializer(serializers.ModelSerializer):
    responders=ResponderSerializer(many=True, read_only=True)
    answers=AnswerSerializer(many=True, read_only=True)
    class Meta:
        model=Question
        fields=['id','name','answers','responders']
