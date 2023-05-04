from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage),
    path('item/<int:pk>', views.exact_product)
]

