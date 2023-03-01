from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice


# Create your views here.

def index(request):
    return HttpResponse("Hello World")


def test(request):
    return HttpResponse("<h1>Hello World</h1><hr><p>Đây là một ví dụ kiểm thử thôi</p>")


def test_template(request):
    my_name = 'Hoàng'
    my_item = ['Phone', 'Laptop', 'Tablet', 'Love']
    context = {"name": my_name, "item": my_item}
    return render(request, "polls/index.html", context)


def view_question_list(request):
    question_list = Question.objects.all()
    special_lst = get_object_or_404(Question, pk=1)
    context = {"ques_lst": question_list, "spec_lst": special_lst}
    return render(request, "polls/question_list.html", context)


def view_question_detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {"question": question}
    except:
        context = {"question": 'null'}
    return render(request, "polls/question_detail.html", context)

def view_vote_result(request, question_id):

    try:
        choice_id = request.POST["answer"]
        choice = Choice.objects.get(pk=choice_id)
        choice.vote = choice.vote + 1
        choice.save()
    except:
        pass
    finally:
        question = Question.objects.get(pk=question_id)
        choice_list = question.choice_set.all()
        context = {"question": question, "choice_list": choice_list}
        return render(request, "polls/vote_result.html", context)
    pass
