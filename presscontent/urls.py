from django.urls import path, include
from django.views.generic import RedirectView
from presscontent.views import PressContentListAPIView, PressContentDetailAPIView


app_name = "presscontent"


urlpatterns = [
    #path('',  RedirectView.as_view(pattern_name='list')),
    path('list/', PressContentListAPIView.as_view(), name="list"),
    path('detail/<slug:slug>', PressContentDetailAPIView.as_view(), name='detail')
]
