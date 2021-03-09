from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.all()

    return HttpResponse(latest_question_list)

def detail(request, question_id):
    return HttpResponse("you are watching detail view %s " % question_id )

def results(request, question_id):
    return HttpResponse("you are watching results view %s " % question_id )

def vote(request, question_id):
    return HttpResponse("you are watching vote view %s " % question_id)