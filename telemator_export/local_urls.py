from django.conf.urls import url, patterns, include
import navtelemator
urlpatterns = patterns(
    '',
    (r'^telemator/', include('navtelemator.urls')),
)
