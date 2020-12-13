from django.urls import path
from . import views


# appnme="votingapp"
urlpatterns = [
    path('', views.login, name='login'),
    path('capture_image/', views.capture_image, name='capture_image'),
    path('register/', views.register, name='register'),
    path('cast_vote/', views.cast_vote, name='cast_vote'),
    path('response/', views.response, name='response'),
    # path('livefeed/', views.livefeed, name='feed'),
    path('votenow/', views.index, name='index'),
    path('getquery/', views.getquery, name='getquery'),
    path('sortdata/', views.sortdata, name='sortdata'),
    path('livwin/', views.livefeed_window, name='liv_win')
]
