from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
# 카탈로그 애플리케이션에서 경로를 추가하려면 include()를 사용하세요.
from django.conf.urls import include

# 카탈로그 url 맵퍼
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# 기본 URL을 애플리케이션으로 리디렉션하기 위한 URL 맵 추가
from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# 정적 파일(html ,css, javascript)를 제공하는것을 가능하게 하는 코드
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Django 사이트 인증 URL 추가(로그인, 로그아웃, 비밀번호 관리용)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

