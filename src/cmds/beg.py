import random, math, sqlite3
from cmds.randline import random_word
from cmds.users import change_bal
# from users import *

def calc_beg():
    "calculates the amount the amount the user gets when running the beg command. Returns an interger"
    succeed = bool(random.getrandbits(1))
    # succeed = True
    if succeed == True:
        give_precent = round(random.uniform(0, 1), 2)
        give_amount = int(math.floor(300 * give_precent))
    else:
        give_amount = 0
    return(give_amount)

def beg_command(uid):
    "calculates the amount a user gets, edits there balance, and returns a message to display to the user"
    win_amount = calc_beg()
    random_name = random_word('data/fakenamelist.txt')
    if win_amount != 0:
        change_bal(uid, win_amount)
        return random_name + " gave you " + str(win_amount) + " coins!"
    else:
        return random_name + " said fuck off lol"


#Testing values to make sure winrate semi-reasonable
#uncomment for debugging
# lowest = 500
# _max = 0
# mean = int()
# sample_size = 1_000
# timesLost = 0
# for _ in range(sample_size):
#     num = calc_beg()
#     print(num)
#     mean += num
#     if lowest > num and num != 0:
#         lowest = num
#     if _max < num:
#         _max = num
#     if num == 0:
#         timesLost += 1
# print("max: " + str(_max))
# print("mean: " + str(mean//sample_size))
# print("min: " + str(lowest))
# print("win%: " + str(float(float(sample_size - timesLost) / float(sample_size) )))
