from django.urls import path
from . import views

urlpatterns = [
    path('signal-test/', views.signal_test_view, name='signal_test'),
    path('transaction-test/', views.test_transaction_view, name='transaction_test'),
    path('rectangle-test/', views.test_rectangle_view, name='rectangle_test'),
]
