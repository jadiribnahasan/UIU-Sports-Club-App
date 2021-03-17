from django.urls import path, include
from . import views
from .views import PlayerProfileView

app_name = "tten"

urlpatterns = [
    path("", views.homepage, name="Home"),
    path("matches/", views.matches, name="Matches"),
    path("teams/", views.teams, name="Teams"),
    path('team/<int:pk>/', views.teamdetails, name="TeamDetails"),
    path('player/<int:pk>/', PlayerProfileView.as_view(), name="PlayerDetails"),
    path("batsmanranking/", views.batsmanRank, name="BatsmanRanking"),
    path("bowlerranking/", views.bowlerRank, name="BowlerRanking"),
    path("pointtable/", views.pointtable, name="PointTable"),
    path("fixtures/", views.fixture, name="Fixture"),

]
