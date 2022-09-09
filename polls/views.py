from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Poll
from django.contrib import messages
from .forms import PollForm
# Create your views here.

def feedback(request,article_name_id):
    form = PollForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        poll=form.save(commit=False)

        # there is an error in the below line
        ## poll.article_name_id = request.article_name_id e
        poll.save()

        messages.success(request,"Evaluation has been successfully created")
        return redirect("index")

    poll = get_object_or_404(Poll)
    context = {'poll':poll,'form':form}
    return render(request,'polls/feedback.html',context)

def success(request):
    return render(request,'polls/success.html')




"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
"""
"""
def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/feedback.html', {'question': question})
"""
"""
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/feedback.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



"""
