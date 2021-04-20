import random, math, sqlite3, time
from cmds.randline import random_word
from cmds.users import change_bal

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
    can_beg_bool, time_to_beg = can_beg(uid)
    time_to_beg = int(60 - time_to_beg)

    if can_beg_bool == False:
        if time_to_beg >= 60:
            time_to_beg = int(time_to_beg/60)
            return "Slow down! You can beg again in " + str(time_to_beg) + " minutes."
        else:
            return "Slow down! You can beg again in " + str(time_to_beg) + " seconds."
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
    if c.fetchone() == None:
        c.execute("INSERT INTO users VALUES (:uid, 0, :time)", {'uid': uid, 'time': int(time.time())})
        c.execute("SELECT begLastIssued FROM users WHERE uid= :uid", {'uid': uid})
        conn.commit()
        conn.close()
        return True
    else:
        c.execute("SELECT begLastIssued FROM users WHERE uid= :uid", {'uid': uid})
        lastused = c.fetchone()[0]
        if lastused == None:
            lastused = 0
        time_sinced_used = int(time.time()) - lastused
        if time_sinced_used >= 60:
            c.execute("UPDATE users SET begLastIssued = :time WHERE uid = :uid", {'uid': uid, 'time': int(time.time())})
            conn.commit()
            conn.close()
            return True, time_sinced_used
        else:
            conn.commit()
            conn.close()
            return False, time_sinced_used


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
