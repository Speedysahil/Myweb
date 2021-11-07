from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name ="Blog"),
    path('blogpost/<int:id>', views.blogpost , name ="BlogPost")
]