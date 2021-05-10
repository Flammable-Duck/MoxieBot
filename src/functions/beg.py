import math
import random
import sqlite3
import time

from functions.randline import random_word
from functions.users import change_bal


def calc_beg():
    "calculates the amount the amount the user gets when running the beg command. Returns an interger"
    succeed = bool(random.getrandbits(1))
    # succeed = True
    if not succeed:
        return 0
    give_precent = round(random.uniform(0, 1), 2)
    return int(math.floor(300 * give_precent))

def beg_command(uid):
    "calculates the amount a user gets, edits there balance, and returns a message to display to the user"
    win_amount = calc_beg()
    random_name = random_word('data/fakenamelist.txt')
    can_beg_bool, time_to_beg = can_beg(uid)
    time_to_beg = int(60 - time_to_beg)

    if can_beg_bool == False:
        if time_to_beg < 60:
            return "Slow down! You can beg again in " + str(time_to_beg) + " seconds."
        time_to_beg = int(time_to_beg/60)
        return "Slow down! You can beg again in " + str(time_to_beg) + " minutes."
    if win_amount != 0:
        change_bal(uid, win_amount)
        return random_name + " gave you " + str(win_amount) + " coins!"
    else:
        return random_name + " said fuck off lol"

def can_beg(uid):
    "returns True if a user can beg. If True, it resets the time"
    conn = sqlite3.connect('data/users.db')
    c = conn.cursor()
    c.execute("SELECT uid FROM users WHERE uid= :uid", {'uid': uid})
    if c.fetchone() is not None:
        return _extracted_from_can_beg_13(c, uid, conn)
    c.execute("INSERT INTO users VALUES (:uid, 0, :time)", {'uid': uid, 'time': int(time.time())})
    c.execute("SELECT begLastIssued FROM users WHERE uid= :uid", {'uid': uid})
    conn.commit()
    conn.close()
    return True

def _extracted_from_can_beg_13(c, uid, conn):
    c.execute("SELECT begLastIssued FROM users WHERE uid= :uid", {'uid': uid})
    lastused = c.fetchone()[0]
    if lastused is None:
        lastused = 0
    time_sinced_used = int(time.time()) - lastused
    if time_sinced_used < 60:
        return _extracted_from_can_beg_20(conn, False, time_sinced_used)

    c.execute("UPDATE users SET begLastIssued = :time WHERE uid = :uid", {'uid': uid, 'time': int(time.time())})
    return _extracted_from_can_beg_20(conn, True, time_sinced_used)

def _extracted_from_can_beg_20(conn, arg1, time_sinced_used):
    conn.commit()
    conn.close()
    return arg1, time_sinced_used


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
