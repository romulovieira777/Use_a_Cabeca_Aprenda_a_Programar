"""
# My Solution:
scores = [
    60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44,
    18, 41, 53, 55, 61, 51, 44
]

for score in scores:
    print('Bubble solution #' + str(scores.index(score)), 'score:', score)

total_bubbles_tests = len(scores)
print(f'Bubbles tests: {total_bubbles_tests}')

highest_score = max(scores)
print(f'Highest bubble score: {highest_score}')

best_solutions = []

for score in scores:
    if score == highest_score:
        best_solutions.append(scores.index(score))

print(f'Solutions with the highest score: {best_solutions}')
"""

# Book Solution:
scores = [
    60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44,
    18, 41, 53, 55, 61, 51, 44
]

i = 0

length = len(scores)

while i < length:
    print('Bubble solution #' + str(i), 'score:', scores[i])
    i = i + 1
