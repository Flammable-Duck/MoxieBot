from random import randint
import math

def wheel_spin():
    num = randint(0, 36)
    if num == 0:
        color = "green"
    elif (num % 2) == 0:
        color = "red"
    else:
        color = "black"
    return (num, color)

def play_roulette(uid, bet, amount):
    spin_num, spin_color = wheel_spin()
    if bet == "black" and spin_color == "black":
        winnings = math.ceil(amount*1)
        message = "You won!\nYou won %d coins"%winnings
    elif bet == "red" and spin_color == "red":
        winnings = math.ceil(amount*1)
        message = "You won!\nYou won %d coins"%winnings
    elif bet == "green" and spin_color == "green":
        winnings = math.ceil(amount*10)
        message = "You won!\nYou won %d coins"%winnings
    elif bet == "low" and spin_num <= 18:
        winnings = math.ceil(amount*1)
        message = "You won!\nYou won %d coins"%winnings
    elif bet == "high" and spin_num >= 18:
        winnings = math.ceil(amount*1)
        message = "You won!\nYou won %d coins"%winnings
    elif bet == spin_num:
        winnings = amount
        message = "You won!\nYou won %d coins"%winnings
    elif bet == 0 and spin_num == 0:
        winnings = math.ceil(amount*10)
        message = "You won!\nYou won %d coins"%winnings
    else:
        winnings = -amount
        message = "You lost! :(\nYou lost %d coins"%winnings
    return (winnings, message)