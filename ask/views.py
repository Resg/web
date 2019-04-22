from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Tag, Usr, QuestionLike
from django.core.paginator import Paginator


def paginate(objects_list, page):
    paginator = Paginator(objects_list, 3)
    return paginator.get_page(page)


def question_list(request):
    questions = Question.objects.new()
    tags = Tag.objects.all()[:7]
    users = Usr.objects.all()[:7]
    page = request.GET.get('page')
    paginator = paginate(questions, page)
    return render(request, 'ask/questions.html', {
        'questions': paginator,
        'tags': tags, 'users': users,
    })


def question_rate(request):
    questions = Question.objects.hot()
    tags = Tag.objects.all()[:7]
    users = Usr.objects.all()[:7]
    page = request.GET.get('page')
    paginator = paginate(questions, page)
    return render(request, 'ask/questions.html', {
        'questions': paginator,
        'tags': tags, 'users': users,
    })


def add_question(request):
    questions = Question.objects.new()
    tags = Tag.objects.all()[:7]
    users = Usr.objects.all()[:7]
    return render(request, 'ask/add_question.html', {
        'questions': questions,
        'tags': tags,
        'users': users,
    })


def question_answ(request, questionsname):
    tags = Tag.objects.all()[:7]
    current_question = get_object_or_404(Question, id=questionsname)
    answ = current_question.answer_set.order_by('-rating')
    page = request.GET.get('page')
    paginator = paginate(answ, page)
    users = Usr.objects.all()[:7]
    return render(request, 'ask/question_answ.html', {
        'tags': tags,
        'users': users,
        'cur_que': current_question,
        'questions': paginator,
    })


def tag_srch(request, tag_s):
    current_tag = get_object_or_404(Tag, title=tag_s)
    questions = Question.objects.filter(tags=current_tag)
    page = request.GET.get('page')
    paginator = paginate(questions, page)
    tags = Tag.objects.all()[:7]
    users = Usr.objects.all()[:7]
    return render(request, 'ask/tag_srch.html', {
        'questions': paginator,
        'tag': current_tag, 'tags': tags,
        'users': users
    })


def usr_settings(request):
    questions = Question.objects.new()
    tags = Tag.objects.all()[:7]
    users = Usr.objects.all()[:7]
    return render(request, 'ask/usr_settings.html', {
        'questions': questions,
        'tags': tags,
        'users': users,
    })


def log_in(request):
    questions = Question.objects.hot()
    tags = Tag.objects.all()[:7]
    users = Usr.objects.all()[:7]
    return render(request, 'ask/log_in.html', {
        'questions': questions,
        'tags': tags,
        'users': users,
    })


def registr(request):
    questions = Question.objects.hot()
    tags = Tag.objects.all()[:7]
    users = Usr.objects.all()[:7]
    return render(request, 'ask/registr.html', {
        'questions': questions,
        'tags': tags,
        'users': users,
    })


