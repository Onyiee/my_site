from collections import defaultdict

from django.shortcuts import render
from polls.models import Question


# Create your views here.


def index(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, "polls/index.html", context)
