from django.db import models

# Create your models here.
class Genre(models.Model):
    """책 장르를 대표하는 모델."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """Model 객체를 표현하기 위한 문자열입니다."""
        return self.name

from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Language(models.Model):
    """언어(예: 영어, 프랑스어, 일본어 등)를 나타내는 모델"""
    name = models.CharField(max_length=200,
                            unique=True,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def get_absolute_url(self):
        """특정 언어 인스턴스에 액세스하기 위한 URL을 반환합니다."""
        return reverse('language-detail', args=[str(self.id)])

    def __str__(self):
        """Model 객체를 표현하기 위한 문자열(관리 사이트 등에서)"""
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='language_name_case_insensitive_unique',
                violation_error_message = "Language already exists (case insensitive match)"
            ),
        ]


class Book(models.Model):
    """책을 나타내는 모델입니다(책의 특정 사본은 아님)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    # 책에는 저자가 한 명만 있을 수 있지만 저자는 여러 권의 책을 가질 수 있으므로 외래 키가 사용됩니다.
    # 아직 파일에 선언되지 않았기 때문에 객체가 아닌 문자열로 작성합니다.
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # 장르에 많은 책이 포함될 수 있으므로 ManyToManyField가 사용됩니다. 책은 다양한 장르를 다룰 수 있습니다.
    # 장르 클래스는 이미 정의되어 있으므로 위에서 개체를 지정할 수 있습니다.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """객체를 표현하기 위한 문자열입니다."""
        return self.title

    def get_absolute_url(self):
        """이 책의 세부 기록에 액세스하기 위한 URL을 반환합니다."""
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """장르에 대한 문자열을 만듭니다. 관리자에서 장르를 표시하기 위해 필요합니다."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

import uuid # Required for unique book instances
# 사용자 제한
from django.conf import settings
from datetime import date

class BookInstance(models.Model):
    """책의 특정 사본을 나타내는 모델(예: 도서관에서 빌릴 수 있는 책)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    # 책 인스턴스의 기한이 지났는지 알려주기 위해 템플릿에서 호출할 수 있는 속성
    @property
    def is_overdue(self):
        """Determines if the book is overdue based on due date and current date."""
        return bool(self.due_back and date.today() > self.due_back)

    class Meta:
        ordering = ['due_back']
        # 권한 추가
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """Model 객체를 표현하기 위한 문자열입니다."""
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """작가를 대표하는 모델."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """특정 작성자 인스턴스에 액세스하기 위한 URL을 반환합니다."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """Model 객체를 표현하기 위한 문자열입니다."""
        return f'{self.last_name}, {self.first_name}'
