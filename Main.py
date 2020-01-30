import HTMLParser
import JSONParser
import Analyzer
import MatchUtils
import time
import datetime

# matches1 = HTMLParser.parse_from_html("res/games1.html")
# matches2 = HTMLParser.parse_from_html("res/games2.html")
# matches = MatchUtils.combine_matches(matches2, matches1)
# matches.sort(key=lambda x: x.timestamp)
# JSONParser.write_json(matches, "res/matches.json")
# print(len(matches))

matches = JSONParser.read_json("res/matches.json")

maps = Analyzer.map_ranking(matches)
for map, count in sorted(maps.items(), key=lambda item: item[1]):
    print(map + ": " + str(count))

# mates = Analyzer.teammate_ranking(matches, "https://steamcommunity.com/id/AleMax")
# for mate, count in sorted(mates.items(), key=lambda item: item[1]):
#     print(mate + ": " + str(count))




