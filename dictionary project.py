#Eric Schneider
#dictionaries 9/17/18-
import random
import time


strengh=random.choice(range(5,13))
magics=random.choice(range(5,13))
dexteriti=random.choice(range(5,13))
defence=random.choice(range(5,13))
hp= dexteriti*3
#Dictionary


def view_player(Name, Xp, Level, Strength, Magic, Dexterity, Hp, Defense):

    #stat inputs
    player={
        'Name':names,
        'Xp':0,
        'Level':1,
        'Strength':strengh,
        'Magic':magics,
        'Dexterity':dexteriti,
        'Hp':dexteriti*3,
        'Defense':defence,
        }
    return player

#very long and very conveluted encouter with a single monster
def encounter():
    print ('A wild ork stands in your path, there is no turning around and no running away. you must fight.')
    ork_hp==90
    while ork_hp>0:
        attack= input('How will you attack? With [m]agic or with a [s]word?')
        if attack==m:
            spell= input ('What spell? [R]ay of frost: 90% accuracy,[F]lair bolt: 90% accuracy, [Q]uicksand: 30% accuracy, but stops the monster from attacking, [M]agic Missile: 45% accuracy, but does double damage.')
            if spell==R:
                damage==magics
                print('You do%s'%damage %'%s points of damage)
                ork_hp-=damage
                print
            elif

#Start up screen
names= input('Please enter the name you wish to be called by.')
print(view_player('name', 'xp', 'level', 'strengh', 'magics', 'dexteriti', 'hp', 'defence'))
time.sleep(5)
print ('you will see your stats in the future whenever you level up.')
time.sleep(5)
print('You can play for as long as you wish to, but can only stop after you win a round or die.')
time.sleep(5)
print('Before we begin playing, I must first tell you a couple ground rules.')
print('every time you sustain a hit, you will take damage and your remaining hp will be shown.')
print('You will automatically heal to your max health when you level up.')
print(Strength)
print('this is your strength stat. your ammount of dammage is directly proportional.')
replay=''
#while replay!=n
    #encounter()   
