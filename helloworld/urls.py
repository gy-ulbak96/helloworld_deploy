from django.contrib import admin
from django.urls import path
import basic.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',basic.views.home,name='home'),
]
