from django.urls import path

from . import views

urlpatterns = [
    path('', views.help_request_view, name='customer_form'),
    path('success/', views.success_view, name='success'),
]
