from django.urls import path
from .views import EnvView

urlpatterns = [
    path('env', EnvView.as_view(), name='env'),
]
