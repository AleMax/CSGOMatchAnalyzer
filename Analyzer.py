import time
import csv
import math
import datetime


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


def enemy_ranking(matches, player_number):
    enemies = {}
    for match in matches:
        team = match.get_other_team(match.get_team_from_player(player_number))
        if team is not None:
            for player in team.players:
                if player.link in enemies:
                    enemies[player.link] += 1
                else:
                    enemies[player.link] = 1
        else:
            print("WEIRD MATCH CASE")
    return enemies


def win_loss_count(matches, player_number):
    wins = 0
    ties = 0
    losses = 0
    for match in matches:
        team = match.get_team_from_player(player_number)
        if team.won == 1:
            wins += 1
        elif team.won == 0:
            ties += 1
        elif team.won == -1:
            losses += 1
    print("Won:\t" + str(wins))
    print("Tied:\t" + str(ties))
    print("Lost:\t" + str(losses))


def matches_by_month_csv(matches, filepath):
    months = {}
    for match in matches:
        date = time.localtime(match.timestamp)
        month_string = "1." + str(date.tm_mon) + "." + str(date.tm_year)

        if month_string in months:
            months[month_string] += 1
        else:
            months[month_string] = 1

    with open(filepath, mode="w") as file:
        writer = csv.writer(file)

        writer.writerow(["Month", "Count"])
        writer.writerows(list(months.items()))


def matches_by_time_of_day_csv(matches, filepath):
    minute = [0] * (24 * 60)

    for match in matches:
        date = time.localtime(match.timestamp)
        minute_in_day = date.tm_hour * 60 + date.tm_min
        for i in range(round(match.duration / 60)):
            current_minute = minute_in_day + i
            if current_minute < len(minute):
                minute[current_minute] += 1
            else:
                minute[current_minute - len(minute)] += 1

    with open(filepath, mode="w") as file:
        writer = csv.writer(file)

        writer.writerow(["Month", "Count"])
        for i, s in enumerate(minute):
            ho = math.floor(i / 60)
            mi = math.floor(i - ho * 60)
            writer.writerow([str(ho) + ":" + str(mi), s])


def wait_time_per_day_interpolated_csv(matches, filepath):
    days = {}
    for match in matches:
        time_stamp = time.gmtime(match.timestamp)
        day = datetime.datetime(time_stamp.tm_year, time_stamp.tm_mon, time_stamp.tm_mday,
                                12, 0, 0, 0, tzinfo=datetime.timezone.utc).timestamp()
        if day not in days:
            days[day] = 0.0

    for day in days:
        sum_coefficients = 0
        sum_values = 0
        for match in matches:
            day_difference = abs(math.floor((match.timestamp - day) / (24*60*60)))
            coefficient = 1 / math.pow(day_difference + 1, 2)
            sum_coefficients += coefficient
            value = match.waitTime * coefficient
            sum_values += value

        days[day] = sum_values / sum_coefficients

    with open(filepath, mode="w") as file:
        writer = csv.writer(file)

        writer.writerow(["Month", "Count"])
        for key in days:
            tim = time.gmtime(key)
            da = str(tim.tm_mday)
            mo = str(tim.tm_mon)
            yr = str(tim.tm_year)
            if len(da) == 1:
                da = "0" + da
            if len(mo) == 1:
                mo = "0" + mo

            writer.writerow([da + "." + mo + "." + yr, days[key]])


def map_win_percentage_since(matches, player_number, timestamp):
    maps = {}
    for match in matches:
        if match.timestamp > timestamp:
            if match.map not in maps:
                maps[match.map] = [0.0, 0.0]
            maps[match.map][0] += match.get_team_from_player(player_number).score
            maps[match.map][1] += match.get_other_team(player_number).score

    for m in maps:
        sum_of_rounds = (maps[m][0] + maps[m][1])
        maps[m][0] /= sum_of_rounds
        maps[m][1] /= sum_of_rounds

    return maps


def map_win_percentage_since_by_full_match(matches, player_number, timestamp):
    maps = {}
    for match in matches:
        if match.timestamp > timestamp:
            if match.map not in maps:
                maps[match.map] = [0.0, 0.0, 0.0]
            outcome = match.get_team_from_player(player_number).won
            if outcome == 1:
                maps[match.map][0] += 1
            elif outcome == 0:
                maps[match.map][1] += 1
            elif outcome == -1:
                maps[match.map][2] += 1

    for m in maps:
        sum_of_matches = (maps[m][0] + maps[m][1] + maps[m][2])
        maps[m][0] /= sum_of_matches
        maps[m][1] /= sum_of_matches
        maps[m][2] /= sum_of_matches

    return maps


def win_percentage_with_player(matches, timestamp, player1, player2):
    wins = 0.0
    ties = 0.0
    losses = 0.0
    for match in matches:
        if match.timestamp > timestamp and match.has_player(player1) and match.has_player(player2):
            outcome = match.get_team_from_player(player1).won
            if outcome == 1:
                wins += 1
            elif outcome == 0:
                ties += 1
            elif outcome == -1:
                losses += 1

    sum_of_matches = wins + ties + losses
    wins /= sum_of_matches
    ties /= sum_of_matches
    losses /= sum_of_matches

    print(str(round(wins * 10000) / 100) + "\t" + str(round(ties * 10000) / 100) + "\t"
          + str(round(losses * 10000) / 100))
    print(sum_of_matches)
