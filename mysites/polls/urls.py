from django.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
]