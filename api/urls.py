from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path(r'bills/fetch', views.BillView.as_view(), name='bills'),
    path(r'bills/fetchReceipt', views.ReceiptView.as_view(), name='receipt'),
]
