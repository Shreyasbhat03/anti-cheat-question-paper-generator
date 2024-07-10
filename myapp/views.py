import random
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm

def generate_question_papers_data():
    questions = Question.objects.all()
    question_papers = []
    answer_keys = []

    for _ in range(30):
        question_paper = []
        answer_key = []

        for question in questions:
            speed = random.uniform(30, 80)
            duration = random.uniform(1, 10)
            
            distance = speed * duration
            question_paper.append({
                'question_text': question.question_text,
                'speed': speed,
                'duration': duration,
            })
            answer_key.append({
                'question_text': question.question_text,
                'answer': distance,
            })

        question_papers.append(question_paper)
        answer_keys.append(answer_key)

    return question_papers, answer_keys

def generate_question_papers(request):
    question_papers, answer_keys = generate_question_papers_data()

    zipped_data = zip(question_papers, answer_keys)

    context = {
        'zipped_data': zipped_data,
    }
    return render(request, 'index.html', context)

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('generate_question_papers')
    else:
        form = QuestionForm()
    
    return render(request, 'questions.html', {'form': form})

def display_answer_key(request):
    _, answer_keys = generate_question_papers_data()

    context = {
        'answer_keys': answer_keys,
    }
    return render(request, 'answer.html', context)
