import Match


def combine_matches(matches1, matches2):
    matches = []
    for match in matches1:
        timestamp = match.timestamp
        found = False
        for m in matches:
            if timestamp == m.timestamp:
                found = True
                break
        if not found:
            matches.append(match)

    for match in matches2:
        timestamp = match.timestamp
        found = False
        for m in matches:
            if timestamp == m.timestamp:
                found = True
                break
        if not found:
            matches.append(match)
    return matches
