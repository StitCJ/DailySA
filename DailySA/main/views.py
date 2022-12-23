from django.shortcuts import render
import random
from .models import Problem

# Create your views here.
def index(request):
    items = list(Problem.objects.all())
    ran = random.choice(items)
    pnum = ran.pk
    problem = ran.problem
    options = ran.options.split("\n")
    random.shuffle(options)
    answer = ran.answer

    return render(request,'main/index.html', {'pnum': pnum, 'problem': problem, 'o1': options[0], 'o2': options[1], 'o3': options[2], 'o4': options[3], 'answer': answer})

def result(request):
    select = request.GET['select']
    answer = request.GET['answer']
    if select == answer :
        return render(request, 'main/correct.html')
    else :
        pnum = request.GET['pnum']
        problem = Problem.objects.get(pk=pnum)
        question = problem.problem
        options = problem.options.split("\n")
        return render(request, 'main/false.html', {'pnum': pnum, 'problem': question, 'o1': options[0], 'o2': options[1], 'o3': options[2], 'o4': options[3], 'answer': answer, 'select': select})