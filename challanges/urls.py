from django.urls import path

from . import views

urlpatterns = [
    path("<int:month>", views.monthly_response_by_number),
    path("<str:month>", views.monthly_response, name='monthly-challanges'),
]
