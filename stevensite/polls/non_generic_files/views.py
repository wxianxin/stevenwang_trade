from django.shortcuts import render

from django.http import HttpResponse
from .models import Question

################################################################################
################################################################################
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
################################################################################
# from django.template import loader
# 
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     # The context is a dictionary mapping template variable names to Python objects.
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
################################################################################
# shortcut: render()
# Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # The context is a dictionary mapping template variable names to Python objects.
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

################################################################################
################################################################################
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
################################################################################
# from django.http import Http404
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
################################################################################
# A shortcut: get_object_or_404()

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager.
    return render(request, 'polls/detail.html', {'question': question})
################################################################################
################################################################################
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
################################################################################
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
################################################################################
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
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

# request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
# Note that Django also provides request.GET for accessing GET data in the same way.

# After incrementing the choice count, the code returns an HttpResponseRedirect rather than a normal HttpResponse. HttpResponseRedirect takes a single argument: the URL to which the user will be redirected.

# As the Python comment above points out, you should always return an HttpResponseRedirect after successfully dealing with POST data.

# reverse() takes the name of the URL patter and will the a string of the URL like '/polls/3/results/'

# race condition: The code for our vote() view does have a small problem. It first gets the selected_choice object from the database, then computes the new value of votes, and then saves it back to the database. If two users of your website try to vote at exactly the same time, this might go wrong: The same value, let’s say 42, will be retrieved for votes. Then, for both users the new value of 43 is computed and saved, but 44 would be the expected value.
