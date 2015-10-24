from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^genres$', views.GenresView.as_view(), name='genres'),
]
