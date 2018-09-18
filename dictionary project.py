#Eric Schneider
#dictionaries 9/17/18-
import random
import time

name= input('Please enter the name you wish to be called by.')

#Dictionary
def build_player(name, xp, level, strength, magic, dexterity, hp):

    #stat inputs
    player={
        'name':name,
        'xp':0,
        'level':1,
        'strength':random.choice(range(5,13)),
        'magic':random.choice(range(5,13)),
        'dexterity':random.choice(range(5,13)),
        'hp':dexterity*3,
        }
    return ("Here is your character.")
    return player

build_player('name', 'xp', 'level', 'strength', 'magic', 'dexterity', 'hp')
time.sleep(5)

