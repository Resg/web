from django.urls import path
from . import views


urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('hot', views.question_rate, name='question_rate'),
    path('ask', views.add_question, name='add_question'),
    path('question', views.question_answ, name='question_answ'),
    path('tag', views.tag_srch, name='tag_srch'),
    path('settings', views.usr_settings, name='usr_settings'),
    path('login', views.log_in, name='log_in'),
    path('signup', views.registr, name='registr'),
    path('questions/<questionsname>/', views.question_answ, name='question'),
    path('tag/<tag_s>/', views.tag_srch, name='tag__'),
]
