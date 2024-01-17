lista = ['banana', 'pineapple', 'coconut', 'strawberry']

lista.sort()
print(lista)


def bubble_sort_ascendente(scores):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(scores) - 1):
            if scores[i] > scores[i + 1]:
                temp = scores[i]
                scores[i] = scores[i + 1]
                scores[i + 1] = temp
                swapped = True


bubble_sort_ascendente(lista)
print(lista)


def bubble_sort_descendente(scores):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(scores) - 1):
            if scores[i] < scores[i + 1]:
                temp = scores[i]
                scores[i] = scores[i + 1]
                scores[i + 1] = temp
                swapped = True


bubble_sort_descendente(lista)
print(lista)
