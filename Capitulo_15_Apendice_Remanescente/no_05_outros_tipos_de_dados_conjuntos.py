set = {1, 3.14159264, False, 77}
print(set)

set.add(99)
print(set)

set.remove(1)
print(set)

even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
prime = {1, 3, 5, 7}

even_and_prime = even.intersection(prime)
print(even_and_prime)

odd_and_prime = odd.intersection(prime)
print(odd_and_prime)

even_or_prime = even.union(prime)
print(even_or_prime)
