from django.urls import path
from .views import MoviesView

app_name = 'movies'

urlpatterns = [
    path('', MoviesView.as_view(), name='get-movies'),
]
