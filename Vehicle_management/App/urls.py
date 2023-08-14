from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import VehicleList, VehicleCreate, VehicleUpdate, VehicleDelete, VehicleView, CustomLoginView, RegisterView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', VehicleList.as_view(), name='vehicle'),
    path('create/', VehicleCreate.as_view(), name='create'),
    path('update/<int:pk>/', VehicleUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', VehicleDelete.as_view(), name='delete'),
    path('details/<int:pk>/', VehicleView.as_view(), name='details'),
]