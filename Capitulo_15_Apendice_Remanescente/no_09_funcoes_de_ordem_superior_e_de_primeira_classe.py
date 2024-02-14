def pluralize(str):
    def helper(word):
        return word + 's'
    return helper(str)


val = pluralize('girl')
print(val)


def addition_maker(n):
    def maker(x):
        return n + x
    return maker


add_two = addition_maker(2)

val = add_two(1)
print(val)
