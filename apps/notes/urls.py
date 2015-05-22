__author__ = 'Alok'

from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from apps.notes import views

urlpatterns = [
    url(r'^notes$', views.NoteList.as_view()),
    url(r'^note/(?P<pk>[0-9]+)$', views.NoteDetail.as_view()),
    url(r'^users$', views.NoteList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)$', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)