from django.contrib import admin
# 게시글(Post) Model을 불러옵니다
from .models import Problem, Discussion

# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Problem)
admin.site.register(Discussion)
