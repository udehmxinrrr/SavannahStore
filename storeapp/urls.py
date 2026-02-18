from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from storeapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Home'),
    path('gallery/', views.gallery, name='Gallery'),
    path('services/', views.services, name='Services'),

]
