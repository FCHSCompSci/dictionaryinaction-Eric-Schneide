#Eric Schneider
#dictionaries 9/17/18-
import random

strength= random.choice(range(5,21))
magic=random.choice(range(5,21))
dexterity=random.choice(range(5,21))
hp=dexterity*3
def build_player(xp, level, strength,magic, dexterity, hp):
    player={
        'xp':0,
        'level':1,
        'strenght':strength,
        'magic':magic,
        'dexterity':dexterity,
        'hp':hp,
        }
print("Here is your character.")
print(build_player())


