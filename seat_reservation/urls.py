from django.contrib import admin
from django.urls import path
from reservations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.seat_list, name='seat_list'),
    path('reserve/<int:seat_id>/', views.reserve_seat, name='reserve_seat'),
]
