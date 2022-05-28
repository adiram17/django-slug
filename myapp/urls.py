from django.urls import path
from . import views

urlpatterns = [
    path('book/<slug:slug>', views.book, name = 'book')
]