from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Bad Request use another route")


def language(request):
    return HttpResponse("My favorite language is Python.")


def system(request):
    return HttpResponse("my favorite System is ios.")


def ide(request):
    return HttpResponse("my favorite ide is IntelillJ")

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
#
# def sum(request, number1, number2):
#     return HttpResponse(('the sum of ', number1, "and", number2))