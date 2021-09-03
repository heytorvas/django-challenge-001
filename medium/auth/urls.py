from django.conf.urls import url
from django.urls import path, include
from auth.views import RegisterApi
urlpatterns = [
      path('', RegisterApi.as_view()),
]