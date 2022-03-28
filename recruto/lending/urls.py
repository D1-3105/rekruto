from django.urls import path, re_path
from .views import HelloView

urlpatterns = [
    #path('<list:args>/', HelloView.as_view()),
    path('', HelloView.as_view(), name='m'),
]