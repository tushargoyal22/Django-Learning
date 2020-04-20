from django.shortcuts import render
from main import models
from django.views.generic import (
    ListView,
    DetailView
)

# Create your views here.

class Index(ListView):

    model = models.Question
    template_name = 'main/index.html'
    # By default the context_object_name that is passed is lowercase model name _ list
    # that is question_list in this case

class QuestionDetailView(DetailView):
    model = models.Question
    template_name = "main/question.html"
