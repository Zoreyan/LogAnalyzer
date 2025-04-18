from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('products/', ProductsView.as_view(), name='products'),
    path('payments/', PaymentsView.as_view(), name='payments'),
    path('shipping/', ShippingView.as_view(), name='shipping'),
]