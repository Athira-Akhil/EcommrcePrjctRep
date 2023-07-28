from django.urls import path
from . import views

app_name='Search_app'

urlpatterns=[
    path('',views.searchResult,name='searchResult'),
]