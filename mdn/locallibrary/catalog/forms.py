import datetime

from django import forms
from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _ # 장고 버전 이슈

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        # forms.Form에서 상속받음(cleaned_data) 사용자가 입력한 날짜가 형식에 맞는지 판별
        data = self.cleaned_data['renewal_date']

        # 날짜가 과거가 아닌지 확인합니다.
        if data < datetime.date.today():
            raise ValidationError(('Invalid date - renewal in past'))

        # 날짜가 허용 범위(오늘부터 +4주) 내에 있는지 확인합니다.
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(('Invalid date - renewal more than 4 weeks ahead'))

        # 항상 정리된 데이터를 반환하는 것을 기억하세요.
        return data
