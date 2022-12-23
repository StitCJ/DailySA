from django.shortcuts import render
from .models import Solved
from main.models import Problem

# Create your views here.
def mypage(request):
    user = request.user
    user_solved = Solved.objects.filter(user_id=user)
    n = 0
    for i in user_solved :
        n += 1
    return render(request, 'userstat/mypage.html', {'solved': n})