from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/leads/', include('leads.urls')),
    url(r'^api/auth/', include('accounts.urls')),
    url(r'^', include('frontend.urls'))
]
