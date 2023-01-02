from django.shortcuts import render, redirect
import random
from .models import Problem, Discussion
from userstat.models import Solved

# Create your views here.
def index(request):
    parm = request.GET.get("pnum", "")
    print(parm)
    if parm == "" :
        items = list(Problem.objects.all())
        ran = random.choice(items)
    else :
        ran = Problem.objects.get(pk=parm)
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

def new_post(request):
    if request.method == 'POST':
        pnum = request.POST.get('pnum')
        new_discussion=Discussion(
            postname=request.POST.get('postname'),
            content=request.POST.get('content'),
            problem_id=Problem.objects.get(pk=pnum)
            )
        new_discussion.save()
        return render(request,'main/index.html')
    else :
        pnum = request.GET['pnum']
    return render(request, 'main/new_post.html', {'pnum': pnum})

def discussion(request):
    discussions = Discussion.objects.all()
    return render(request, 'main/discussion.html', {'discussions': discussions})

def detail(request, discussion_id):
    discussion = Discussion.objects.get(pk=discussion_id)
    postname = discussion.postname
    content = discussion.content
    problem_id = discussion.problem_id.pk
    return render(request, 'main/detail.html', {'postname': postname, 'content': content, 'problem_id': problem_id})