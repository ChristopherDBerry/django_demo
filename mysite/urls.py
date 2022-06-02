from django.contrib import admin
from django.urls import path, include

from supportdesk import views as supportdesk_views

urlpatterns = [
    path('', supportdesk_views.home),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('supportdesk/', include('supportdesk.urls')),
]
