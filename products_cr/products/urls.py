from django.urls import path
from products_cr.products import views


urlpatterns = [
    path("api/products/", views.ProductAPIList.as_view()),
]
