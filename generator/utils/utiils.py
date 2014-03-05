from random import randint


def shuffle(collection):
    """Shuffle the collection"""

    for i in xrange(1, len(collection)):
        j = randint(0, i)
        if i != j:
            collection[i], collection[j] = collection[j], collection[i]


def reservoir_sampling(collection, k):
    """Returns k randomly selected elements from the given collection.
    k has to be positive and greater than 0.
    """
    n = len(collection)

    if k < 0:
        raise Exception('Incorrect input (k = %d)' % k)

    if k > n:
        raise Exception('Collection has only %d element(s)' % n)

    result = collection[:k]
    for i in xrange(k, n):
        j = randint(0, i)
        if j < k:
            result[j] = collection[i]

    return result