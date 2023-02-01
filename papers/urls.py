# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from papers import views

urlpatterns = [
    path('papers/', views.PaperList.as_view()),
    path('papers/<int:pk>/', views.PaperDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)