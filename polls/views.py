from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
 
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'poll.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise HttpResponse("Question does not exist")
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Calculate total votes for the question
    total_votes = sum(choice.votes for choice in question.choice_set.all())

    # Calculate the percentage for each choice
    choices_with_percentage = []
    for choice in question.choice_set.all():
        percentage = (choice.votes / total_votes) * 100 if total_votes > 0 else 0
        choices_with_percentage.append({
            'choice_text': choice.choice_text,
            'votes': choice.votes,
            'percentage': percentage,
        })

    context = {
        'question': question,
        'choices_with_percentage': choices_with_percentage,
    }

    return render(request, 'results.html', context)

def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args =(question.id, )))