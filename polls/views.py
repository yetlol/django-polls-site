from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404

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
    # use shortcuts get_object_or_404() whice is use
    # models get() function, if not found, will raise 404()
    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question is not exist.')
    context = {
      'question': question
    }
    # return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
