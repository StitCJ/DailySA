from django.shortcuts import render
from .models import Solved
from main.models import Problem

# Create your views here.
def mypage(request):
    user = request.user
    user_solved = Solved.objects.filter(user_id=user)
    not_solved = Solved.objects.exclude(user_id=user)
    n = 0
    pklst = []
    for i in user_solved :
        pklst.append(i.problem_id.pk)
        n += 1
    nn = 0
    npklst = []
    for i in not_solved :
        npklst.append(i.problem_id.pk)
        nn += 1
    return render(request, 'userstat/mypage.html', {'nsolved': n, 'pklst': pklst, 'nnsolved': nn, 'npklst': npklst})