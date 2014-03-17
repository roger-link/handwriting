from django.conf.urls import patterns, url
from handwriting.views import HandwritingView

urlpatterns = patterns('',
    url(r'^', HandwritingView.as_view()),
)
