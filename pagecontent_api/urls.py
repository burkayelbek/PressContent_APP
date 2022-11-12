from django.urls import path
from django.views.generic import RedirectView
from pagecontent_api.views import PressContentListAPIView, PressContentDetailAPIView

urlpatterns = [
    path('',  RedirectView.as_view(pattern_name='list')),
    path('list/', PressContentListAPIView.as_view(), name="list"),
    path('detail/<pk>', PressContentDetailAPIView.as_view(), name='detail')
]
