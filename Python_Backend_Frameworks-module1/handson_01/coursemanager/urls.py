from django.contrib import admin
from django.urls import path
from courses.views import hello_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', hello_view),
]