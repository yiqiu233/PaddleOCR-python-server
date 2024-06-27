from django.urls import include, path
from paddleApp import admin, views
# ProjectName/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('paddleApp/',include('paddleApp.urls'))
]