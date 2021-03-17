from django.shortcuts import render
from .models import Match, Team, Player, Fixture
from django.views import generic


def homepage(request):
    return render(request, "home.html")


def matches(request):

    matches = Match.objects.all()
    matchSorted = sorted(
        matches, key=lambda match: match.matchNo, reverse=True)

    return render(request, 'match_history.html', {'matches': matchSorted})


def teams(request):
    context = {
        'teams': Team.objects.all()
    }
    return render(request, 'teams.html', context)


def teamdetails(request, pk):
    team = Team.objects.filter(pk=pk).first()
    players = Player.objects.filter(team=pk)
    context = {
        'team': team,
        'players': players
    }
    return render(request, 'teamdetails.html', context)


class PlayerProfileView(generic.DetailView):
    model = Player
    template_name = 'player_details.html'


def batsmanRank(request):
    batsmans = Player.objects.all()
    batsmanSorted = sorted(
        batsmans, key=lambda batsman: batsman.run, reverse=True)
    return render(request, 'batsmanrank.html', {'batsmans': batsmanSorted[:10]})


def bowlerRank(request):
    bowlers = Player.objects.all()
    bowlerSorted = sorted(
        bowlers, key=lambda bowler: bowler.wicket, reverse=True)
    return render(request, 'bowlerrank.html', {'bowlers': bowlerSorted[:10]})


def pointtable(request):
    teams = Team.objects.all()
    teamsSorted = sorted(
        teams, key=lambda team: team.point, reverse=True)
    return render(request, 'pointtable.html', {'teams': teamsSorted})


def fixture(request):
    fixtures = Fixture.objects.all()
    fixtureSorted = sorted(
        fixtures, key=lambda fixture: fixture.id, reverse=True)
    return render(request, 'fixture.html', {'fixtures': fixtureSorted})
