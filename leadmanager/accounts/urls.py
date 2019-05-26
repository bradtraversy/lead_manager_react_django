from django.conf.urls import url, include
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

urlpatterns = [
  url(r'^register$', RegisterAPI.as_view()),
  url(r'^login$', LoginAPI.as_view()),
  url(r'^user$', UserAPI.as_view()),
  url(r'^logout$', knox_views.LogoutView.as_view(), name='knox_logout'),
  url(r'^', include('knox.urls'))
]
