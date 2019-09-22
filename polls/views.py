from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Question
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_data')[:5]
    output=', '.join(q.question_text for q in latest_questions)
    context={'latest_questions':latest_questions}
    return render(request,'polls/index.html',context)

def details(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/details.html',{'question':question})

def results(request,question_id):
    return HttpResponse("this is the result of question: %s"%question_id)

def vote(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice=question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request,'polls/details.html',{'question':question,'error_message':'Please select a option'})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args={question.id}))