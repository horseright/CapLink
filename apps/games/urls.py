from django.urls import path

from . import views


app_name = "games"

urlpatterns = [
    path("gameList/", views.GameListView.as_view(), name="game-list"),
    path("detail/<slug:pk>/", views.GameDetailView.as_view(), name="detail")
]
