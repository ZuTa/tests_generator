from random import randint


def shuffle(collection):
    for i in xrange(1, len(collection)):
        j = randint(0, i)
        if i != j:
            collection[i], collection[j] = collection[j], collection[i]