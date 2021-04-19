import random, math
# from users import *

def beg_command(uid):
    # succeed = bool(random.getrandbits(1))
    succeed = True
    if succeed == True:
        give_precent = round(random.uniform(0, 1), 2)
        give_amount = int(math.floor(300 * give_precent))
    else:
        give_amount = 0
    return(give_amount)

# Testing values to make sure its semi-reasonable
# uncomment for debugging
# lowest = 500
# _max = 0
# mean = int()
# sample_size = 1_000
# for _ in range(sample_size):
#     num = beg_command("")
#     print(num)
#     mean += num
#     if lowest > num:
#         lowest = num
#     if _max < num:
#         _max = num
# print("max: " + str(_max))
# print("mean: " + str(mean//sample_size))
# print("min: " + str(lowest))
