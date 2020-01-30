import datetime
import Match


def parse_from_html(file):
    file = open(file, "r")
    lines = file.readlines()
    matches = []
    for i in range(len(lines)):
        if "csgo_scoreboard_inner_left" in lines[i]:
            matches.append(Match.Match())
            match = matches[-1]

            match.map = lines[i+3].split("\t")[6][12:]

            timestamp_string = lines[i+7].split("\t")[6]
            year = int(timestamp_string.split("-")[0])
            month = int(timestamp_string.split("-")[1])
            day = int(timestamp_string.split("-")[2].split(" ")[0])
            hour = int(timestamp_string.split(" ")[1].split(":")[0])
            minute = int(timestamp_string.split(" ")[1].split(":")[1])
            second = int(timestamp_string.split(" ")[1].split(":")[2])
            match.timestamp = datetime.datetime(year, month, day, hour, minute, second, 0,
                                                tzinfo=datetime.timezone.utc).timestamp()

            wait_time_string = lines[i+11].split("\t")[6].split(" ")[2]
            match.waitTime = 0
            match.waitTime += int(wait_time_string.split(":")[0]) * 60
            match.waitTime += int(wait_time_string.split(":")[1])

            duration_string = lines[i+15].split("\t")[6].split(" ")[2]
            match.duration = 0
            parts = duration_string.split(":")
            if len(parts) == 3:
                match.duration += int(parts[0]) * 3600
                match.duration += int(parts[1]) * 60
                match.duration += int(parts[2])
            elif len(parts) == 2:
                match.duration += int(parts[0]) * 60
                match.duration += int(parts[1])
            else:
                match.duration += int(parts[0])

            if "Viewers" in lines[i+19]:
                match.viewers = int(lines[i + 19].split("\t")[6].split(" ")[1])
            else:
                match.viewers = 0

            match.team1 = Match.Team()
            match.team2 = Match.Team()

            player_count = 0
            current_line_offset = 0
            while player_count < 10:
                if "<td class=\"inner_name\">		<div class=\"playerAvatar" in lines[i + current_line_offset]:
                    if player_count < 5:
                        match.team1.players.append(Match.Player())
                        player = match.team1.players[-1]
                    else:
                        match.team2.players.append(Match.Player())
                        player = match.team2.players[-1]

                    player.number = int(lines[i + current_line_offset + 1].split("\"")[7])
                    player.link = lines[i + current_line_offset].split("\"")[5]
                    player.username = lines[i + current_line_offset + 1].split(">")[2].split("</a>")[0][:-3]

                    player.ping = int(lines[i + current_line_offset + 3].split(">")[1].split("<")[0])
                    player.kills = int(lines[i + current_line_offset + 4].split(">")[1].split("<")[0])
                    player.assists = int(lines[i + current_line_offset + 5].split(">")[1].split("<")[0])
                    player.deaths = int(lines[i + current_line_offset + 6].split(">")[1].split("<")[0])
                    if "★" in lines[i + current_line_offset + 7]:
                        mvps = lines[i + current_line_offset + 7].split(">")[1].split("<")[0]
                        if len(mvps) > 1:
                            player.MVPs = int(mvps[1:])
                        else:
                            player.MVPs = 1
                    else:
                        player.MVPs = 0
                    if "%" in lines[i + current_line_offset + 8]:
                        player.HSP = int(lines[i + current_line_offset + 8].split(">")[1].split("<")[0][:-1])
                    else:
                        player.HSP = 0
                    player.score = int(lines[i + current_line_offset + 9].split(">")[1].split("<")[0])

                    player_count += 1

                elif "<tr><td colspan=\"8\" class=\"csgo_scoreboard_score\">" in lines[i + current_line_offset]:
                    scores = lines[i + current_line_offset].split(">")[2].split("<")[0]
                    match.team1.score = int(scores.split(" ")[0])
                    match.team2.score = int(scores.split(" ")[2])

                current_line_offset += 1

            if match.team1.score > match.team2.score:
                match.team1.won = 1
                match.team2.won = -1
            elif match.team1.score < match.team2.score:
                match.team1.won = -1
                match.team2.won = 1
            else:
                match.team1.won = 0
                match.team2.won = 0
    return matches
