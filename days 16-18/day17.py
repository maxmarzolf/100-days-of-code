import random

names = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

capitalized_names = [name.title() for name in names]
print(capitalized_names)


def gen_pairs():
    first_choice = random.choice(names)
    second_choice = random.choice(names)
    pair = first_choice + ' is working with ' + second_choice
    print(pair)
    yield pair


my_first_generator = gen_pairs()
for _ in range(10):
    next(my_first_generator)
