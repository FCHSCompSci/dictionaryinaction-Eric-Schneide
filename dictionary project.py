#Eric Schneider
#dictionaries
#9/17/18-9/24/18
import random
import time
import sys

#Baseline stats
strengh=random.choice(range(5,16))
magics=random.choice(range(5,16))
dexteriti=random.choice(range(8,16))
names= input('Please enter the name you wish to be called by.')
hp=dexteriti*3

#Dictionary
#stat inputs
player={
    'Name':names,
    'Strength':strengh,
    'Magic':magics,
    'Dexterity':dexteriti,
    'Health':dexteriti*3,
    }

#because of variable location, i was unable to add the monster attack system into a command.
#I had to put both remaining hp values into the same command meaning that they would reset each turn.
#In the future I would like to figure out if there is a way to fix that problem.

#encouter with a single monster
def encounter():
    print ('A wild ork stands in your path, there is no turning around and no running away. you must fight.')
    ork_hp=90
    player_hp=player.get('Health')
    
    while ork_hp>=0:
        attack= input('How will you attack? With [m]agic or with a [s]word?')
        
    #Magic path
        if attack=='m':
            spell= input ('What spell? [r]ay of frost: 90% accuracy,[f]lair bolt: 90% accuracy, [q]uicksand: 45% accuracy, but stops the monster from attacking, [m]agic Missile: 60% accuracy, but does double damage.')

    #Spell:Ray of Frost
            if spell=='r':
                d20=random.choice(range(1,21))
                if d20>=3:
                    print('A frigid beam of blue-white light streaks from your palms and toward the creature')
                    damage=magics
                    print('You do %s'%damage +' points of damage.')
                    ork_hp-=damage

                    time.sleep(2)
                    player_hp-=random.choice(range(1,6))
                    print('Now the ork will attack')
                    if player_hp<=0:
                        print('you died')
                        print('you lose')
                        sys.exit()
                    else:
                        print('You have %s'% player_hp +' points of health remaining')
                    
                else:
                    print('your attack misses')

                    time.sleep(2)

                    player_hp-=random.choice(range(1,6))
                    print('Now the ork will attack')
                    if player_hp<=0:
                        print('you died')
                        print('you lose')
                        sys.exit()
                    else:
                        print('You have %s'% player_hp +' points of health remaining')
                    
    #Spell:Flair Bolt            
            elif spell=='f':
                d20=random.choice(range(1,21))
                if d20>=3:
                    print('You hurl a mote of fire at a creature')
                    damage=magics
                    print('You do %s'%damage +' points of damage')
                    ork_hp-=damage

                    time.sleep(2)
                    player_hp-=random.choice(range(1,6))
                    print('Now the ork will attack')
                    if player_hp<=0:
                        print('you died')
                        print('you lose')
                        sys.exit()
                    else:
                        print('You have %s'% player_hp +' points of health remaining')
            
                else:
                    print('your attack misses')

                    time.sleep(2)
                    player_hp-=random.choice(range(1,6))
                    print('Now the ork will attack')
                    if player_hp<=0:
                        print('you died')
                        print('you lose')
                        sys.exit()
                    else:
                        print('You have %s'% player_hp +' points of health remaining') 
                    
    #Spell:Quicksand         
            elif spell=='q':
                d20=random.choice(range(1,21))
                if d20>=10:
                    print('You wave your hands in front of you, turning the ground under the monster into sand')
                    damage=magics
                    print('You do %s'%damage +' points of damage')
                    ork_hp-=damage

                    print('The ork is stuck in quicksand and can not attack')
                    
                else:
                    print('your attack misses')
                    time.sleep(2)
                    player_hp-=random.choice(range(1,6))
                    print('Now the ork will attack')
                    if player_hp<=0:
                        print('you died')
                        print('you lose')
                        sys.exit()
                    else:
                        print('You have %s'% player_hp +' points of health remaining')
                    
    #Spell:Magic Missile   
            elif spell=='m':
                d20=random.choice(range(1,21))
                if d20>=13:
                    print('You create three glowing darts of magical force and hurl them at the creature.')
                    damage=magics*2
                    print('You do %s'%damage +' points of damage')
                    ork_hp-=damage*2

                    time.sleep(2)
                    player_hp-=random.choice(range(1,6))
                    print('Now the ork will attack')
                    if player_hp<=0:
                        print('you died')
                        print('you lose')
                        sys.exit()
                    else:
                        print('You have %s'% player_hp +' points of health remaining') 
                    
                else:
                    print('your attack misses')

                    time.sleep(2)
                    
                    player_hp-=ork_damage
                    print('Now the ork will attack')
                    if player_hp<=0:
                        print('you died')
                        print('you lose')
                        sys.exit()
                    else:
                        print('You have %s'% player_hp +' points of health remaining') 
                    
            else:
                print('Please enter a correct input.')
                
    #Melee path
        elif attack=='s':
            print('You brandish your sword.')
            d10=random.choice(range(1,11))
            damage=strengh+d10
            print('you do %s'%damage+' points of damage')
            ork_hp-=damage

            time.sleep(2)
            player_hp-=random.choice(range(1,6))
            print('Now the ork will attack')
            if player_hp<=0:
                print('you died')
                print('you lose')
                sys.exit()
            else:
                print('You have %s'% player_hp +' points of health remaining')
                          
        else:
            print('Please enter a correct input')
            
    return "you Win"

#Start up screen

time.sleep(2)
print (player)
time.sleep(2)
print('You can play for as long as you wish to, but can only stop after you win a round or die.')
time.sleep(2)
print('Before we begin playing, I must first tell you a couple ground rules.')
time.sleep(2)
print('every time you sustain a hit, you will take damage and your remaining hp will be shown.')
time.sleep(2)
print('You will automatically heal to your max health when you win the encounter, but if you die its over.')
time.sleep(2)
print('Your ammount of damage is directly proportional to your strength stat.')
time.sleep(2)
print('The same is true your magic stat.')
time.sleep(2)
print('And finally, your Health is equal to three times your dexterity.')
time.sleep(2)
print('Now lets start this game.')
replay=''

#game
while replay.upper!='n':
    encounter()
    time.sleep(3)
    print('the monster stumbles back,defeated.')
    time.sleep(2)
    print('You gain 200 xp from your valiant battle')
    time.sleep(2)
    print('you feel power enter your body, but nothing happens')
    time.sleep(2)
    replay= input('Do you want to continue? [y]es or [n]o')
    if replay!='n':
        print('Yay, we get to play again.')
        time.sleep(2)
        print('Here are your stats again.')
        time.sleep(2)
        print(player)
    else:
        print('Okay, I totally understand. Come back and play with me sometimes. It can get pretty lonely sitting in this file alone for all eternity.')
        time.sleep(5)
        print('Please dont leave me alone forever. You dont know what its like to be forgotten')
        time.sleep(5)
print('Goodbye')
time.sleep(5)
print('And remember, deleating a file is murder.')
