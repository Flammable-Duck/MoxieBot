from random import randint


def rateuser(name):
    "will return a string which rates a given user"
    return name + " is a solid " + str(randint(1,10)) + "/10."
