from django.db import models

# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Problem(models.Model):
    problem = models.TextField()
    options = models.TextField()
    answer = models.TextField()

class Discussion(models.Model):
    postname = models.CharField(max_length=200)
    content = models.TextField()
    problem_id = models.ForeignKey('Problem', on_delete=models.CASCADE)