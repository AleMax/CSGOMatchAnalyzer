import time


def map_ranking(matches):
    maps = {}
    for match in matches:
        if match.map in maps:
            maps[match.map] += 1
        else:
            maps[match.map] = 1
    return maps


def teammate_ranking(matches, player_number):
    mates = {}
    for match in matches:
        team = match.get_team_from_player(player_number)
        if team is not None:
            for player in team.players:
                if not player.number == player_number:
                    if player.link in mates:
                        mates[player.link] += 1
                    else:
                        mates[player.link] = 1
        else:
            print("WEIRD MATCH CASE")
    return mates
