
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('mybiodata/', include('mybiodata.urls')),

    path('admin/', admin.site.urls),
]
