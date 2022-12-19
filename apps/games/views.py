from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Game, GameTag

# Create your views here.


class GameDetailView(DetailView):
    model = Game
    template_name = "frontend/games/detail.html"


class GameListView(ListView):
    model = Game
    template_name = "frontend/games/game-list.html"
    extra_context = {"tags": GameTag.objects.all()}
