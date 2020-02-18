class Player(object):
    def __init__(self):
        self.number = 0
        self.link = ""
        self.username = ""
        self.ping = -1
        self.kills = 0
        self.assists = 0
        self.deaths = 0
        self.MVPs = 0
        self.HSP = 0
        self.score = 0


class Team(object):
    def __init__(self):
        self.score = 0
        self.won = 0
        self.players = []


class Match(object):
    def __init__(self):
        self.map = ""
        self.timestamp = 0 #in seconds since epoch
        self.waitTime = 0 #in seconds
        self.duration = 0 #in seconds
        self.viewers = 0
        self.team1: Team
        self.team2: Team

    def get_team_from_player(self, number):
        for player in self.team1.players:
            if number == player.number:
                return self.team1
        for player in self.team2.players:
            if number == player.number:
                return self.team2
        return None

    def get_other_team(self, team):
        if team is self.team1:
            return self.team2
        else:
            return self.team1

    def has_player(self, number):
        if self.get_team_from_player(number) is None:
            return False
        else:
            return True

