"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views as web_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', web_views.index, name="index"),
    path('web/sns', web_views.sns, name="sns"),
    path('web/charge', web_views.charge, name="charge"),
    path('web/fraud', web_views.fraud, name="fraud"),
    path('web/fraud/oneclick_fraud', web_views.oneclick_fraud, name="oneclick_fraud"),
    path('web/security', web_views.security, name="security"),
    path('web/security/security_exp', web_views.security_exp, name="security_exp"),
    path('quiz1', web_views.quiz1, name="quiz1"),
    path('quiz2', web_views.quiz2, name="quiz2"),
    path('test', web_views.test, name="test"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
