from django.conf.urls import patterns, url
from question import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
     url(r'^$', views.IndexView.as_view(), name='index'),
     url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
     url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
     url(r'^(?P<question_id>\d+)/voted/$', views.voted, name='voted'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
