from django.db import models
from django.contrib.auth.models import User

"""
모델 정의

질문 모델
- 제목 : 질문 제목필드
- 내용 : 제목에 대한 상세한 내용
- 생성일 : 질문 작성일자

답변 모델
- 질문에 대한 참조키 생성(일대다) : CASCADE방식으로 질문이 삭제되면 관련된 답변 모두 삭제
- 내용 : 답변 내용
- 생성일 : 답변 작성일자
"""


# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_question"
    )
    subject = models.CharField(max_length=200)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateField()
    voter = models.ManyToManyField(User, related_name="voter_question")  # 추천인 추가

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_answer"
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateField()
    voter = models.ManyToManyField(User, related_name="voter_answer")
