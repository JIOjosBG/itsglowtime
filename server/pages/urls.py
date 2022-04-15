from django.urls import path
from .views import homepage

urlpatterns = [
    # ex: /polls/
    path('', homepage, name='home'),
]