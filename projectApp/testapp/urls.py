from django.contrib import admin
from django.urls import path, include

from . import views
from django.urls import path
from django.contrib import admin
from .views import HomePageView

app_name = 'testapp'
# path,function names,rename
urlpatterns = [
    # path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('', HomePageView.as_view(), name='home'),
]
