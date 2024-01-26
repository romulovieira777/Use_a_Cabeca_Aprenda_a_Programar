marbles = [10, 13, 39, 14, 41, 9, 3]


def compute_sum(list):
    sum = 0

    for number in list:
        sum += number

    return sum


print("The total is", compute_sum(marbles))
