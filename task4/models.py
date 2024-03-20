from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import FileExtensionValidator

ALLOWED_IMAGE_EXTENSIONS = ["png", "jpg", "jpeg", "bmp", "gif"]


class PlayerPosition(models.TextChoices):
    POSITION = "position",
    FORWARD = "forward",
    MIDFIELDER = "midfielder",
    GOALKEEPER = "goalkeeper",
    DEFENDER = "defender",


class GenderType(models.TextChoices):
    MAN = "erkak",
    WOMAN = "ayol",
    NOT_MENTION = "ixtiyoriy"


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InternationalLeague(models.TextChoices):
    UEFA = "champion league"
    UEL = "europe  league"
    EKL = "konference league"


class GameLocationType(models.TextChoices):
    HOME = "home"
    AWAY = "away"


class Country(models.Model):
    title = models.CharField(max_length=64)


class Stadium(models.Model):
    title = models.CharField(max_length=127)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Player(models.Model):
    full_name = models.CharField(max_length=127)
    age = models.PositiveIntegerField(validators=(
        MinValueValidator(16), MaxValueValidator(40)))

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_country")
    market_value = models.PositiveIntegerField()

    gender = models.CharField(choices=GenderType.choices, default=GenderType.NOT_MENTION, max_length=20)
    position = models.CharField(choices=PlayerPosition.choices, default=PlayerPosition.POSITION, max_length=32)

    current_club = models.ForeignKey("FootballClub", on_delete=models.CASCADE, related_name="player_club")

    def __str__(self):
        return self.full_name


class PlayerStatistic(models.Model):

    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player_statistic")
    minutes_played = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)
    goals = models.PositiveIntegerField(default=0)
    assist = models.PositiveIntegerField(default=0)


class FootballClub(models.Model):
    title = models.CharField(max_length=127)
    logo = models.FileField(validators=[FileExtensionValidator(allowed_extensions=ALLOWED_IMAGE_EXTENSIONS)])

    is_favourite = models.BooleanField(default=False)
    league = models.ForeignKey("League", on_delete=models.CASCADE, related_name="current_league")

    def __str__(self):
        return self.title


class Transfer(models.Model):
    club_from = models.ForeignKey(FootballClub, on_delete=models.CASCADE, related_name="previous_club")
    club_to = models.ForeignKey(FootballClub, on_delete=models.CASCADE, related_name="current_club")

    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="transfering_player")
    transfer_value = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.transfer_value


class Season(models.Model):
    season = models.CharField(max_length=10)


class League(models.Model):
    title = models.CharField(max_length=127)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name="country_leagues", null=True, blank=True)

    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="league_season")

    def __str__(self):
        return self.title


class Referee(models.Model):
    title = models.CharField(max_length=127)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country_referee")

    def __str__(self):
        return self.title


class RefereeStatistic(models.Model):
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE, related_name="referee_statistic")
    number_of_games = models.PositiveIntegerField(default=0)

    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.referee


class Game(models.Model):

    club1 = models.ForeignKey(FootballClub, on_delete=models.CASCADE, related_name="opponent1")
    club2 = models.ForeignKey(FootballClub, on_delete=models.CASCADE, related_name="opponent2")

    date = models.DateTimeField(auto_now_add=True)


class GameStatistic(models.Model):

    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="league_game")
    round = models.PositiveIntegerField(validators=(
        MinValueValidator(1), MaxValueValidator(38)))

    referee = models.ForeignKey(Referee, on_delete=models.CASCADE, related_name="game_referee")
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name="game_stadium")

    attendance = models.PositiveIntegerField()


class Situation(models.Model):
    minutes = models.PositiveIntegerField()
    title = models.CharField(max_length=127)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player_situation")

    game = models.ForeignKey(GameStatistic, on_delete=models.CASCADE, related_name="game_situation")
