# 순서중요! 장고쉘을 파일로 실행하려면 먼저 세팅파일을 불러와야함.
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()


from pybo.models import Question, Answer
from django.utils import timezone
def run():
    # 질문 생성
    # q = Question(subject = 'pybo가 무엇인가요?', content= 'pybo에 대해서 알고 싶습니다.', create_date = timezone.now())
    # q.save()
    # print(q.id)

    # for i in range(300):
    #     q = Question(subject = f'{i+1}번째 질문을 생성합니다', content= f'{i+1}번째 질문에 대한 답변입니다.', create_date = timezone.now())
    #     q.save()
    #     print(q.id)


    # 질문 조회
    print('질문 모델의 모든 레코드를 나열합니다.')
    for i in Question.objects.all():
        print(f'질문:{i.subject} --> 답변:{i.content}')

if __name__ =='__main__':
    run()
