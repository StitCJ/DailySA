from django.shortcuts import render
from .models import Solved
from main.models import Problem

# Create your views here.
def mypage(request):
    user = request.user
    user_solved = Solved.objects.filter(user_id=user)
    problems = Problem.objects.all()
    n = 0
    pklst = []
    for i in user_solved :
        pklst.append(i.problem_id.pk)
        n += 1
    nn = 0
    npklst = []
    for i in problems :
        if problems.pk  not in pklst :
            npklst.append(i.problem_id.pk)
            nn += 1
    return render(request, 'userstat/mypage.html', {'nsolved': n, 'pklst': pklst, 'nnsolved': nn, 'npklst': npklst})