from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from question.models import Choice
from question.models import Question
from django.core.urlresolvers import reverse

class IndexView(generic.ListView):
    template_name = 'question/index.html'
    context_object_name = 'last_questions'

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'question/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'question/results.html'


def voted(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'question/detail.html', {
            'question': p,
            'error_message': "It seems you do not choose, try to press harder",
        })
    else:
        selected_choice.voted += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(p.id,)))
