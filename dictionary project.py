#Eric Schneider
#dictionaries 9/17/18-
import random
import time

#Baseline stats
xp=0
strengh=random.choice(range(5,13))
magics=random.choice(range(5,13))
dexteriti=random.choice(range(5,13))
defence=random.choice(range(5,13))
hp=dexteriti*3


#Dictionary
def view_player(Name, Xp, Level, Strength, Magic, Dexterity, Hp, Defense):

    #stat inputs
    player={
        'Name':names,
        'Xp':xp,
        'Level':1,
        'Strength':strengh,
        'Magic':magics,
        'Dexterity':dexteriti,
        'Hp':hp,
        'Defense':defence,
        }
    return player

#very long and very conveluted encouter with a single monster
def encounter():
    print ('A wild ork stands in your path, there is no turning around and no running away. you must fight.')
    ork_hp=90
    while ork_hp>=0:
        attack= input('How will you attack? With [m]agic or with a [s]word?')
        
    #Magic path
        if attack=='m':
            spell= input ('What spell? [r]ay of frost: 90% accuracy,[f]lair bolt: 90% accuracy, [q]uicksand: 35% accuracy, but stops the monster from attacking, [m]agic Missile: 50% accuracy, but does double damage.')

    #Spell:Ray of Frost
            if spell=='r':
                d20=random.choice(range(1,21))
                if d20>=3:
                    print('A frigid beam of blue-white light streaks from your palms and toward the creature')
                    damage=magics
                    print('You do %s'%damage +' points of damage.')
                    ork_hp-=damage

                    monster_attack()

                else:
                    print('your attack misses')
                    time.sleep(5)

                    monster_attack()
                    
    #Spell:Flair Bolt            
            elif spell=='f':
                d20=random.choice(range(1,21))
                if d20>=3:
                    print('You hurl a mote of fire at a creature')
                    damage=magics
                    print('You do %s'%damage +' points of damage')
                    ork_hp-=damage

                    monster_attack()
                    
                else:
                    print('your attack misses')
                    time.sleep(5)

                    monster_attack()
                    
    #Spell:Quicksand         
            elif spell=='q':
                d20=random.choice(range(1,21))
                if d20>=8:
                    print('You wave your hands in front of you, turning the ground under the monster into sand')
                    damage=magics
                    print('You do %s'%damage %'%s points of damage')
                    ork_hp-=damage

                    print('The ork is stuck in quicksand and can not attack')
                    
                else:
                    print('your attack misses')
                    time.sleep(5)

                    monter_attack()
                    
    #Spell:Magic Missle   
            elif spell=='m':
                d20=random.choice(range(1,21))
                if d20>=11:
                    print('You create three glowing darts of magical force and hurl them at the creature.')
                    damage=magics
                    print('You do %s'%damage %'%s points of damage')
                    ork_hp-=damage*2
                    time.sleep(5)

                    monster_attack()
                    
                else:
                    print('your attack misses')
                    time.sleep(5)

                
                    monster_attack()
                    
            else:
                print('Please enter a correct input.')
                
    #Melee path
        elif attack=='s':
            print('You brandish your sword.')
            time.sleep(3)
            d10=random.choice(range(1,11))
            damage=strengh+d10
            print('you do %s'%damage+' points of damage')
            ork_hp-=damage
            time.sleep(5)


            monster_attack()
            
        else:
            print('Please enter a correct input')
            
    return "you Win"


def monster_attack():
    print('Now the ork will attack')
    ork_damage=7-defence/2
    time.sleep(5)
    print('You take %s'% ork_damage +' damage')
    player_hp-=ork_damage
    time.sleep(5)
    print('You have %s'% hp %'%s points of health remaining')

#player_hp=view_player[hp]
 
#Start up screen
names= input('Please enter the name you wish to be called by.')
#time.sleep(5)
print(view_player('name', 'xp', 'level', 'strengh', 'magics', 'dexteriti', 'hp', 'defence'))
#time.sleep(5)
print ('you will see your stats in the future whenever you level up.')
#time.sleep(5)
print('You can play for as long as you wish to, but can only stop after you win a round or die.')
#time.sleep(5)
print('Before we begin playing, I must first tell you a couple ground rules.')
#time.sleep(5)
print('every time you sustain a hit, you will take damage and your remaining hp will be shown.')
#time.sleep(5)
print('You will automatically heal to your max health when you level up.')
#time.sleep(5)
print('Your ammount of dammage is directly proportional to your strength stat.')
#time.sleep(5)
print('The same is true your magic stat.')
#time.sleep(5)
print('Half of your defence is equal to the amount of damage that will not affect you.')
#time.sleep(5)
print('And finally, your Health is equal to three times yur dexterity.')
#time.sleep(5)
print('Now lets start this game.')
replay=''
#game

while replay.upper!='N':

    encounter()
    print('you see 200 xp rise from the monsters dead corpse. without thinking of how bad an idea it is though, you take it.')
    xp+=200
    if xp>100:
        print('you leveled up')
        strengh+=random.choice(range(5,13))
        magics+=random.choice(range(5,13))
        dexteriti+=random.choice(range(5,13))
        defence+=random.choice(range(5,13))
        hp=dexteriti*3
        print('Your stats increase')
        print(view_player('name', 'xp', 'level', 'strengh', 'magics', 'dexteriti', 'hp', 'defence'))
    else:
        time.sleep(5)
    replay= input('Do you want to continue? [Y] or [N]')
    
