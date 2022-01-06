from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_of_months),
    path("<int:month>", views.monthly_response_by_number),
    path("<str:month>", views.monthly_response, name='monthly-challenges'),
]
