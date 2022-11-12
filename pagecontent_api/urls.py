from django.urls import path
from pagecontent_api.views import test_api

urlpatterns = [
    path('homepage/',test_api, name="hoempage"),
]
