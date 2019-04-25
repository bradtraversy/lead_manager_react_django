from django.conf.urls import url, include
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

urlpatterns = [
  url('', include('knox.urls')),
  url('/register', RegisterAPI.as_view()),
  url('/login', LoginAPI.as_view()),
  url('/user', UserAPI.as_view()),
  url('/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]