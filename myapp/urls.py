from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_question_papers, name='generate_question_papers'),
    path('add/', views.add_question, name='add_question'),
      path('ans/', views.display_answer_key, name='display_answer_ke'),
]
