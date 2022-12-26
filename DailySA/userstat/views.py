from django.shortcuts import render
from .models import Solved
from main.models import Problem

# Create your views here.
def mypage(request):
    user = request.user
    user_solved = Solved.objects.filter(user_id=user)
    print(user_solved[0].problem_id.pk)
    n = 0
    for i in user_solved :
        n += 1
    return render(request, 'userstat/mypage.html', {'solved': n})