from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Tag, Usr
from datetime import datetime
from django.core.paginator import Paginator


def paginate(objects_list, request):
    paginator = Paginator(objects_list, 3)
    page = request.GET.get('page')
    return page, paginator


def question_list(request):
    questions = Question.objects.order_by('-create_date')
    tags = Tag.objects.all()
    users = Usr.objects.all()
    page, paginator = paginate(questions, request)
    return render(request, 'ask/tpss.html', {'questions': paginator.get_page(page),
                                             'tags': tags, 'users': users,
                                             })


def question_rate(request):
    questions = Question.objects.order_by('-rating')
    tags = Tag.objects.all()
    users = Usr.objects.all()
    page, paginator = paginate(questions, request)
    return render(request, 'ask/tpss.html', {'questions': paginator.get_page(page),
                                             'tags': tags, 'users': users,
                                             })


def add_question(request):
    questions = Question.objects.filter(create_date__lte=datetime.now())
    tags = Tag.objects.all()
    users = Usr.objects.all()
    return render(request, 'ask/tpp2.html', {'questions': questions, 'tags': tags, 'users': users})


def question_answ(request, questionsname):
    tags = Tag.objects.all()
    current_question = get_object_or_404(Question, title=questionsname)
    answ = current_question.answer_set
    users = Usr.objects.all()
    return render(request, 'ask/tpp3.html', {
        'tags': tags, 'users': users,
        'cur_que': current_question,
        'answer': answ,
    })


def tag_srch(request, tag_s):
    current_tag = get_object_or_404(Tag, title=tag_s)
    questions = Question.objects.filter(tags=current_tag)
    page, paginator = paginate(questions, request)
    tags = Tag.objects.all()
    users = Usr.objects.all()
    return render(request, 'ask/tpp4.html', {'questions': paginator.get_page(page), 'tag': current_tag, 'tags': tags,
                                             'users': users
                                             })


def usr_settings(request):
    questions = Question.objects.filter(create_date__lte=datetime.now())
    tags = Tag.objects.all()
    users = Usr.objects.all()
    return render(request, 'ask/tpp5.html', {'questions': questions, 'tags': tags, 'users': users})


def log_in(request):
    questions = Question.objects.filter(create_date__lte=datetime.now())
    tags = Tag.objects.all()
    users = Usr.objects.all()
    return render(request, 'ask/tpp6.html', {'questions': questions, 'tags': tags, 'users': users})


def registr(request):
    questions = Question.objects.filter(create_date__lte=datetime.now())
    tags = Tag.objects.all()
    users = Usr.objects.all()
    return render(request, 'ask/tpp7.html', {'questions': questions, 'tags': tags, 'users': users})

