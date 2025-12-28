from django.urls import path
from . import views

app_name = "vendor"

urlpatterns = [
    path('register/', views.RegisterVendorView.as_view(), name='register_vendor'),
]
