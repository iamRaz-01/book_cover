from django.urls import path
from .views import bookCover
# from .views import
urlpatterns = [
    path('', bookCover, name='cover'),
]
