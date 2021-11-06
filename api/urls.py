from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('create_responder',create_responder,name='create_responder'),
    path('get_question/<int:pk>',get_question,name='get_question'),
    path('update_answered_questions',update_answered_questions,name='update_answered_questions')

]
