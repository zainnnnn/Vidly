from django.urls import path
from . import views

# by using this we do not need to prefix app name every time in views names
app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail'),
]
