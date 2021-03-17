from django.db import models
from django.utils import timezone


class Team(models.Model):
    teamName = models.CharField(max_length=200)
    played = models.IntegerField()
    won = models.IntegerField()
    draw = models.IntegerField()
    loss = models.IntegerField()
    point = models.IntegerField()

    def __str__(self):
        return self.teamName


class Player(models.Model):

    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    dept_id = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    run = models.IntegerField()
    wicket = models.IntegerField()
    played = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Match(models.Model):
    matchNo = models.CharField(max_length=20, default="0")
    team1 = models.ForeignKey(
        Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(
        Team, related_name='team2', on_delete=models.CASCADE)
    tosswon = models.ForeignKey(
        Team, related_name='tosswon', on_delete=models.CASCADE)
    winnerTeam = models.ForeignKey(
        Team, related_name='winner', default=1, on_delete=models.CASCADE)
    firstInningsRun = models.IntegerField()
    firstInningsWicket = models.IntegerField()
    firstInningsPlayed = models.CharField(max_length=20, default="0 over")
    secondInningsRun = models.IntegerField()
    secondInningsWicket = models.IntegerField()
    secondInningsPlayed = models.CharField(max_length=20, default="0 over")
    winning_status = models.CharField(max_length=200, default="none")

    def __str__(self):
        return self.matchNo


class Fixture(models.Model):
    team1 = models.ForeignKey(
        Team, related_name='teamone', on_delete=models.CASCADE)
    team2 = models.ForeignKey(
        Team, related_name='teamtwo', on_delete=models.CASCADE)
    matchTime = models.CharField(max_length=200, default="none")
