def solution(genres, plays):
    player = {}
    for i, music in enumerate(zip(genres, plays)):
        if music[0] in player:
            player[music[0]].append((music[1], i))
        else:
            player[music[0]] = [(music[1], i)]

    sums = {}
    for key in player:
        s = sum([item[0] for item in player[key]])
        sums[key] = s

    rank = dict(sorted(sums.items(), key=lambda item: item[1], reverse=True))
    result = []

    for genre in rank:
        temp = sorted(player[genre], reverse=True)
        if len(temp) == 1:
            result.append(temp[0][1])
        elif temp[0][0] == temp[1][0]:
            result.append(temp[1][1])
            result.append(temp[0][1])
        else:
            result.append(temp[0][1])
            result.append(temp[1][1])

    return result