from random import choice


def generate_name():
    name, alphabet = '', 'qwertyuiopasdfghjklzxcvbnm'
    for x in range(7):
        name += choice(alphabet)
    return name
