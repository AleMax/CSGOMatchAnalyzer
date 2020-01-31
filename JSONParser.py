import json
import Match


def write_json(matches, file):
    data = {'matches': []}
    for match in matches:
        players1 = []
        for player in match.team1.players:
            players1.append({
                'number': player.number,
                'link': player.link,
                'username': player.username,
                'ping': player.ping,
                'kills': player.kills,
                'assists': player.assists,
                'deaths': player.deaths,
                'MVPs': player.MVPs,
                'HSP': player.HSP,
                'score': player.score
            })
        players2 = []
        for player in match.team2.players:
            players2.append({
                'number': player.number,
                'link': player.link,
                'username': player.username,
                'ping': player.ping,
                'kills': player.kills,
                'assists': player.assists,
                'deaths': player.deaths,
                'MVPs': player.MVPs,
                'HSP': player.HSP,
                'score': player.score
            })

        data['matches'].append({
            'map': match.map,
            'timestamp': match.timestamp,
            'waitTime': match.waitTime,
            'duration': match.duration,
            'viewers': match.viewers,
            'team1': {
                'score': match.team1.score,
                'won': match.team1.won,
                'players': players1
            },
            'team2': {
                'score': match.team2.score,
                'won': match.team2.won,
                'players': players2
            }
        })

    with open(file, 'w') as outfile:
        json.dump(data, outfile)


def read_json(file):
    with open(file) as json_file:
        data = json.load(json_file)
        matches = []
        for m in data["matches"]:
            matches.append(Match.Match())
            match = matches[-1]

            match.map = m["map"]
            match.timestamp = m["timestamp"]
            match.waitTime = m["waitTime"]
            match.duration = m["duration"]
            match.viewers = m["viewers"]

            match.team1 = Match.Team()
            match.team2 = Match.Team()

            match.team1.score = m["team1"]["score"]
            match.team1.won = m["team1"]["won"]
            players1 = m["team1"]["players"]
            for p in players1:
                match.team1.players.append(Match.Player())
                player = match.team1.players[-1]

                player.number = p["number"]
                player.link = p["link"]
                player.username = p["username"]
                player.ping = p["ping"]
                player.kills = p["kills"]
                player.assists = p["assists"]
                player.deaths = p["deaths"]
                player.MVPs = p["MVPs"]
                player.HSP = p["HSP"]
                player.score = p["score"]

            match.team2.score = m["team2"]["score"]
            match.team2.won = m["team2"]["won"]
            players2 = m["team2"]["players"]
            for p in players2:
                match.team2.players.append(Match.Player())
                player = match.team2.players[-1]

                player.number = p["number"]
                player.link = p["link"]
                player.username = p["username"]
                player.ping = p["ping"]
                player.kills = p["kills"]
                player.assists = p["assists"]
                player.deaths = p["deaths"]
                player.MVPs = p["MVPs"]
                player.HSP = p["HSP"]
                player.score = p["score"]

    return matches
