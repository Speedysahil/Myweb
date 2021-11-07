from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='Shopabout'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='TrackingUs'),
    path('search/', views.search, name='Search Us'),
    path("products/<int:my_id>", views.productView, name="ProductView"),
    path('checkout/', views.checkout, name='Checkout'),



]