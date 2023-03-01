from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add_post, name="add_post"),
    path('add/save/', views.save_post, name="save_post"),
    path('email/send/', views.email_view, name="send_email"),
    path('email/send/submit/', views.process, name="send_submit"),

    path('classbaseview/test/', views.index_class.as_view(), name='index_class'),
]
