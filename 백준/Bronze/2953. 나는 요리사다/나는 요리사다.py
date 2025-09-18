parcitipants = 5
score = []

for i in range(parcitipants):
    a, b, c, d = map(int, input().split())
    score.append([a, b, c, d])

total_score = []
for i in range(parcitipants):
    parcitipants_total = sum(score[i])
    total_score.append(parcitipants_total)

winner_score = max(total_score) 
winner_index = total_score.index(winner_score) + 1

print(winner_index, winner_score)