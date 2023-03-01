from django.contrib import admin
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('testtemplate/', views.test_template, name='test_template'),
    path('question/', views.view_question_list, name='question_list'),
    path('question/<int:question_id>', views.view_question_detail, name='question_detail'),
    path('question/<int:question_id>/result', views.view_vote_result, name='vote_result')
]
