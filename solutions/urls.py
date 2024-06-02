from django.urls import path
from solutions.views import ComputerView

urlpatterns = [
    path('computer/', ComputerView.as_view(), name='computer'),
]