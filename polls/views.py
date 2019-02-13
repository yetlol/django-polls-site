from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_questions_list = Question.objects.order_by('pub_date')[:5]
    # output = '<br> '.join([p.question_text for p in latest_questions_list])
    # template = loader.get_template('polls/index.html')
    context = {
      'latest_questions_list': latest_questions_list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
