from django.shortcuts import render
from .models import Solved
from main.models import Problem
from django.contrib.auth.models import User

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
        if i.pk  not in pklst :
            npklst.append(i.pk)
            nn += 1
    return render(request, 'userstat/mypage.html', {'nsolved': n, 'pklst': pklst, 'nnsolved': nn, 'npklst': npklst})

def ranking(request):
    users = User.objects.all()
    solutions = Solved.objects.all()
    rank = {}
    for user in users :
        rank[user.username] = 0
    for solution in solutions :
        rank[solution.user_id.username] += 1
    rank = dict(sorted(rank.items(), key=lambda x: x[1], reverse=True))    
    rank = [rank]
    return render(request, 'userstat/ranking.html', {'rank': rank})