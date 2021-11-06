from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Responder, Question, Answer
from .serializers import ResponderSerializer,QuestionSerializer,AnswerSerializer
# Create your views here.
def index(request):
    return render(request,'api/index.html')

#check if the responder exists or not to send the data
#phone and name are unique so if exists it will continue and
#get the data of the responder other wise create new one
@api_view(['POST'])
def create_responder(request):
    try:
        responder=Responder.objects.get(name=request.data['name'],
                                        phone_number=request.data['phone_number'],
                                        address=request.data['address'],
                                        nationality=request.data['nationality'],
                                        DOB=request.data['DOB'],
                                        gender=request.data['gender'],
                                        )
        serialized_responder=ResponderSerializer(responder)
        return Response(serialized_responder.data)
    except:
        responder_serializer=ResponderSerializer(data=request.data)
        if responder_serializer.is_valid():
            responder_serializer.save()
        return Response(responder_serializer.data)


@api_view()
def get_question(request,pk):
    try:
        question=Question.objects.get(id=pk)
        question_serializer=QuestionSerializer(question)
        serialized_questions=question_serializer.data
        return Response(serialized_questions)
    except:
        data={
        'name':"You finished Questions",
        'answers':[]
        }
        return Response(data)


# submit the anwers of questions
@api_view(['POST'])
def update_answered_questions(request):
    responder=Responder.objects.get(id=request.data['responder_id'])
    question=Question.objects.get(id=request.data['question_id'])
    responder.answered_questions.add(question.id)
    list_of_answers=request.data['list_of_answers']
    for ans in list_of_answers:
        responder.answers.add(ans)
    question_serializer=QuestionSerializer(question)
    return  Response(question_serializer.data)
