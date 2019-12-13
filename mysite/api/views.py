from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from polls.models import Question
from api.serializers import QuestionSerializer
from api.serializers import ChoiceSerializer

class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


"""
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from polls.models import Question, Choice
from api.serializers import QuestionSerializer, ChoiceSerializer


class QuestionList(APIView):
    #get request - all things in django take in a request
    def get(self, request):
        #last 20 questions
        questions = Question.objects.all()[:20]
        #turns it into dta
        data = QuestionSerializer(questions, many=True).data
        
        return Response(data)

class QuestionDetail(APIView):
    #pk - primary key (id) (how it is identified in a database)
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        data = QuestionSerializer(question).data
        return Response(data)

"""