from django.shortcuts import render
import random
from .models import Problem
from userstat.models import Solved

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
    select = request.GET['select'].strip()
    answer = request.GET['answer'].strip()
    user = request.user
    pnum = request.GET['pnum']
    problem = Problem.objects.get(pk=pnum)
    if select == answer and user.username != '':
        user_solved = Solved.objects.filter(user_id=user)
        switch = 0
        for suser in user_solved :
            if suser.problem_id == Problem.objects.get(pk=pnum) :
                switch = 1
                break
        if switch == 0 :
            tsolved = Solved(problem_id=Problem.objects.get(pk=pnum), user_id=user)
            tsolved.save()
        return render(request, 'main/correct.html')
    elif select == answer :
        return render(request, 'main/correct.html')
    else :
        question = problem.problem
        options = problem.options.split("\n")
        return render(request, 'main/false.html', {'pnum': pnum, 'problem': question, 'o1': options[0], 'o2': options[1], 'o3': options[2], 'o4': options[3], 'answer': answer, 'select': select})