from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^genres$', views.GenresView.as_view(), name='genres'),
    url(r'^gallery$', views.GalleryView.as_view(), name='gallery'),
    url(r'^contacts$', views.ContactsView.as_view(), name='contacts'),
]
