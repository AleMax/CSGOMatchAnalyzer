import HTMLParser
import JSONParser
import Analyzer
import MatchUtils
import time
import datetime

# matches1 = HTMLParser.parse_from_html("res/games1.html")
# matches2 = HTMLParser.parse_from_html("res/games3.html")
# matches = MatchUtils.combine_matches(matches2, matches1)
# matches.sort(key=lambda x: x.timestamp)
# JSONParser.write_json(matches, "res/matches.json")
# print(len(matches))

matches = JSONParser.read_json("res/matches.json")

# maps = Analyzer.map_ranking(matches)
# for map, count in sorted(maps.items(), key=lambda item: item[1]):
#     print(map + ": " + str(count))

# mates = Analyzer.teammate_ranking(matches, "https://steamcommunity.com/id/AleMax")
# for mate, count in sorted(mates.items(), key=lambda item: item[1]):
#     print(mate + ": " + str(count))

#enemies = Analyzer.enemy_ranking(matches, 184242319)
#for enemy, count in sorted(enemies.items(), key=lambda item: item[1]):
#    print(enemy + ": " + str(count))

# Analyzer.win_loss_count(matches, 184242319)

# Analyzer.matches_by_month_csv(matches, "res/gamesPerMonth.csv")

# Analyzer.matches_by_time_of_day_csv(matches, "res/gamesByTime.csv")

# Analyzer.wait_time_per_day_interpolated_csv(matches, "res/waitTime.csv")

# maps = Analyzer.map_win_percentage_since(matches, 184242319, 1575162000)
# for m in maps:
#     print(m + "\t" + str(round(maps[m][0] * 10000) / 100))

maps = Analyzer.map_win_percentage_since_by_full_match(matches, 184242319, 1575162000)
for m in maps:
    print(m + "\t" + str(round(maps[m][0] * 10000) / 100) + "\t" + str(round(maps[m][1] * 10000) / 100) + "\t"
          + str(round(maps[m][2] * 10000) / 100))


