# d = {
# 'rohit' : [9,120,105,140,130],
# 'shakib' : [56,78,102,72]
# }
from dask.array import average

player_scores = {}
with open("scores.csv", "r") as f:
    for line in f:
        player,score = line.split(',')
        score = int(score)
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]
for player, score_list in player_scores.items():
    print(player, score_list)
    min_score = min(score_list)
    max_score = max(score_list)
    avg_score = sum(score_list) / len(score_list)

    print(f'{player} ==> Minimum Score = {min_score}, Maximum Score = {max_score}, Average Score = {avg_score}')
