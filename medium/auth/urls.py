from django.urls import path
from auth.views import RegisterApi

urlpatterns = [
      path('', RegisterApi.as_view()),
]