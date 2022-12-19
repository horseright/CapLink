from django.shortcuts import render
from django.views.generic import DetailView

from .models import Order

# Create your views here.


class OrderDetailView(DetailView):
    model = Order
    template_name = 'frontend/order'
