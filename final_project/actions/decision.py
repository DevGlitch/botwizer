import random


def decision(probability):
    """ Function that gives you a decision based on a given probability
    :param probability: float between 0 and 1
    :type: float
    :return: True or False
    :rtype: bool
    """
    if random.random() < probability:
        print("You know what let's do it...")
        return True

    else:
        print("I will pass for this time...")
        return False
