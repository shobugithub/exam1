from django.contrib import admin
from django.urls import path

from blog.views import index, product_detail, customers, customer_detail, add_customer, customer_edit, delete_customer

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path("customers/",customers, name="customers"),
    path("customers", customers, name="customers"),
    # path("customer-detail/",customer_detail, name='customer_detail'),
    path('customer-detail/<int:pk>', customer_detail, name='customer_detail'),
    path('add-customer', add_customer, name='add_customer'),
    path("customer-edit/<int:pk>/", customer_edit,name="edit_customer"),
    path("delete-customer/<int:pk>", delete_customer, name="customer_delete")
]
