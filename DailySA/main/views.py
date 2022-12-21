from django.shortcuts import render
import random
from .models import Problem

# Create your views here.
def index(request):
    items = list(Problem.objects.all())
    ran = random.choice(items)
    problem = ran.problem
    options = ran.options.split()
    random.shuffle(options)
    answer = ran.answer

    return render(request,'main/index.html', {'problem': problem, 'o1': options[0], 'o2': options[1], 'o3': options[2], 'o4': options[3], 'answer': answer})

def result(request):
    select = request.GET['select']
    answer = request.GET['answer']
    if select == answer :
        return render(request, 'main/correct.html')
    else :
        return render(request, 'main/false.html', {'answer': answer, 'select': select})