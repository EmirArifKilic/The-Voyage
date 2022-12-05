def ship_choice():
    print('Choose your S.T.S carefully.')
    time.sleep(1)
    print('1)' + 'Blitz (red and yellow).')
    time.sleep(1)
    print('2)' + 'Deft (blue and silver).')

def blitz():
    print('You approach the red and yellow colored ship.')
    time.sleep(2)
    print('You notice the tag written in front of it.')
    time.sleep(2)
    print('"Blitz"')
    time.sleep(2)
    print('You see that Blitz does not look like a big ship. The glowing red and yellow mixture catches your eye.') 
    time.sleep(2)
    print('Even though it\'s capacity is only 1 person, the acceleration of it must be quite fast, you assume.')
    time.sleep(2)

def deft():
    print('You approach the blue and silver colored ship.')
    time.sleep(2)
    print('You see the name tag at it\'s back.')
    time.sleep(2)
    print('"Deft"')
    time.sleep(2)
    print('This ship has quite the size, you think. It won\'t go very fast.')
    time.sleep(2)
    print('It seems that there are 2 seats on this vessel. The glittering blue and the silver looks nice.')
    time.sleep(2)


import random
import time
print('TheVoyage' + ' is a story based game that features player choice, the consequences of all your in game actions and decisions will impact the past, present and future. Choose wisely…')
time.sleep(6)
print('State your name.')
myName = input()                # asks for their name
time.sleep(1)
print('The year is 20xx.')
time.sleep(2)
print('You are an employee of a private company called "Zeta Mining".')
time.sleep(2)
print('Your mission in the company is studying Earth\'s layers and its contents such as minerals and rocks.')
time.sleep(2)
print('It\'s a messy job but you enjoy it.')
time.sleep(2)
print('One day, while you are in the middle of an analysis process, you receive a phone call.')
time.sleep(2)
print('It is your superior.')
time.sleep(2)
print('"' + myName + ', we are relocating you, to Neptune. Our pioneers have set up a temporary base near the planet. We need you to analyze the gas surrounding it\'s atmosphere."')
time.sleep(5)

print('What do you say to your superior?')     # transfer yes or no
time.sleep(2)
print('1) ' + '"But I have a life here! What about my family? Can\'t you find someone else!?"')
time.sleep(2)
print('2) ' + '"Right away boss."')

job = int(input())
if job == 1:
    print('Not happy with this out of nowhere news, you mutter :')
    time.sleep(2)
    print('"But I..."')
    time.sleep(1)
    print('"No arguing. The decision is effective immediately."')
    time.sleep(2)
    print('"Ugh. Fine."')
    time.sleep(2)
    

elif job == 2:
    print('"Right away boss."')
    time.sleep(1)
print('"You need to take a S.T.S (Space Transportation Ship), which in in the company\'s hangar, to leave the Earth. Get there now." *hangs up*')
time.sleep(3)
print('How will you get to the S.T.S?')                                    # car or bus
time.sleep(2)
print('1)' + 'With a bus')
time.sleep(1)
print('2)' + 'With your own car')
        
vehicle = int(input())                  # Car or Bus
        
if vehicle == 2:
    print('You drove your car to the hangar.')
    time.sleep(3)
elif vehicle == 1:
    print('You took a bus to get to the hangar.')
    time.sleep(3)
print('You\'ve arrived at the main hangar.')
time.sleep(2)
print('In the hangar you see several ships ready to be used. Among them two of them catches your eye.')
time.sleep(2)

print('Which one do you want to look at first?')
time.sleep(2)
print('1)' + 'The glowing red and yellow one.')
time.sleep(2)
print('2)' + 'The glittering blue and silver one.')       
spaceship = int(input())            # Blitz or Deft
            
if spaceship == 1:                  # Starting with Blitz
    print(blitz())
    print('Are you going to choose this S.T.S ?')
    time.sleep(1)
    print('1)' + 'Yes')
    time.sleep(1)
    print('2)' + 'No, I\'ll check the other one first.')
                
    spaceship_pick = int(input())     # asking Confirmation on Blitz


    if spaceship_pick == 2:       # no to Blitz, introducing Deft
        print(deft())
        print(ship_choice())            
        spaceship_confirm = int(input()) # Final decision : Blitz or Deft (blitz to deft)
        mySpaceship = 'Deft'

    elif spaceship_pick == 1:                     # yes to Blitz 
        time.sleep(1)                        
        print('You launched off with "Blitz".')
        mySpaceship = 'Blitz'
                        
elif spaceship == 2:                               # Starting with Deft
    print(deft())
    print('Are you going to choose this S.T.S ?')
    time.sleep(1)
    print('1)' + 'Yes')
    time.sleep(1)
    print('2)' + 'No, I\'ll check the other one first.')
    spaceship_pickD = int(input())   # asking Confirmation on Deft

            
    if spaceship_pickD == 1:     # yes to Deft
        time.sleep(1)
        print('You launched off with "Deft".')
        mySpaceship = 'Deft'

        
    elif spaceship_pickD == 2:     # no to Deft, introducing Blitz
        print(blitz())
        print(ship_choice())
        spaceship_confirm = int(input())    # Final decision : Blitz or Deft (deft to blitz)

        
        if spaceship_confirm == 1:                   # Blitz route
            print('You launched off with "Blitz".')
            mySpaceship = 'Blitz'

        elif spaceship_confirm == 2:                 # Deft route                           
            print('You launched off with "Deft".')
            mySpaceship = 'Deft'


time.sleep(1)
Fuel = 90
print('Fuel = 90')
time.sleep(1)
print('As you are leaving the Earth, you begin to see the stars, all around you.')
time.sleep(3)
print('You watch them in awe, while ' + mySpaceship + ' sails to Neptune automatically.')
time.sleep(3)
print('Passing near Mars, you notice an asteroid belt on your way.')
time.sleep(4)

print('Will you take control of the ship?')
time.sleep(2)
print('Or.')
time.sleep(2)
print('Will you let the ship automatically slip through them, hoping there won\'t be any accidents?')
time.sleep(4)
print('1) ' + 'AI can\'t be trusted on this critical moment, I\'m taking control.')         
time.sleep(2)
print('2) ' + mySpaceship + ' will handle it easily.')                                       
ShipControl = int(input())                                                # Manual or automatic control

if ShipControl == 2:
    print('You let the ship keep the control.')                     # Automatic
    time.sleep(1)
    print('The ship has entered the asteroid belt. (-10 Fuel)')
    time.sleep(1)
    print('Fuel = 80')
    Fuel = 80
    
    chanceAutoBlitz = 80
    chanceAutoDeft = 40

    if mySpaceship == 'Blitz':                    
        if random.randint(0,100) <= chanceAutoBlitz:           # AutoBlitz passed the asteroid belt
            print('The ship begins passing the asteroids one by one.')
            time.sleep(2)
            print('They are close, you can extend your hand to them.')
            time.sleep(2)
            print('As the asteroids flew by, you notice the path has been cleared.')
            time.sleep(2)
            print('You passed the asteroid belt.')
            
        else:                                                  # AutoBlitz failed to pass the  asteroid belt
            print('While you were going through the asteroids...')
            time.sleep(2)
            print('"BOOM"')
            time.sleep(1)
            print('The ship\'s main reactor has been hit by a nearby asteroid and caused a fire.')
            time.sleep(3)
            print('As the fire comes closer to you, you realize that this is the end.')
            time.sleep(3)
            print('UNLUCKY ASTEROID ENDING')
            time.sleep(1)
            print('New achievement unlocked : The unlucky one')
            time.sleep(2)
            exit()
    
    if mySpaceship == 'Deft':
        if random.randint(0,100) <= chanceAutoDeft:               # AutoDeft passed the asteroid belt
            print('The ship begins passing the asteroids one by one.')
            time.sleep(2)
            print('They are close, you can extend your hand to them.')
            time.sleep(2)
            print('As the asteroids flew by, you notice the path has been cleared.')
            time.sleep(2)
            print('You passed the asteroid belt.')
            
        else:                                                     # AutoDeft failed to pass the  asteroid belt
            print('While you were going through the asteroids...')
            time.sleep(2)
            print('"BOOM"')
            time.sleep(1)
            print('The ship\'s main reactor has been hit by a nearby asteroid and caused a fire.')
            time.sleep(3)
            print('As the fire comes closer to you, you realize that this is the end.')
            time.sleep(3)
            print('ASTEROID ENDING.')
            time.sleep(2)
            exit()
    
if ShipControl == 1:
    print('You took control of the ship.')
    time.sleep(1)
    print('"Automated control disabled."')
    time.sleep(2)
    
    print('Ahead lies the asteroid belt. Going through it will not be easy but we will save lots of fuel. (-10 Fuel)')
    time.sleep(3)
    print('"Or I can just go around it..." (-30 Fuel)')
    time.sleep(2)
    print('Which one is it going to be?')
    time.sleep(1)
    print('1) ' + '"Asteroids, here I come." (-10 Fuel)')
    time.sleep(1)
    print('2) ' + 'Not taking the risk. (-30 Fuel)')
    AsteroidQuestion = int(input())                                 # MANUAL : Asteroids or go around

    
    if AsteroidQuestion == 1:                                       # Manual asteroids
        print('You have entered the asteroid belt. (-10 Fuel)')
        time.sleep(2)
        print('Fuel = 80')
        Fuel = 80
        time.sleep(1)

        chanceManualBlitz = 60
        chanceManualDeft = 20

        if mySpaceship == 'Deft':
            if random.randint(0,100) <= chanceManualDeft:            # ManualDeft passed the asteroid belt
                print('You begin passing the asteroids one by one.')
                time.sleep(2)
                print('They are close, you can extend your hand to them.')
                time.sleep(2)
                print('As the asteroids flew by, you notice the path has been cleared.')
                time.sleep(2)
                print('You passed the asteroid belt.')
                
            else:
                print('While you were going through the asteroids...')    # ManualDeft failed to pass the asteroid belt
                time.sleep(2)
                print('"BOOM"')
                time.sleep(1)
                print('The ship\'s main reactor has been hit by a nearby asteroid and caused a fire.')
                time.sleep(3)
                print('As the fire comes closer to you, you realize that this is the end.')
                time.sleep(3)
                print('EXPECTED ASTEROID ENDING.')
                time.sleep(2)
                exit()
                
        elif mySpaceship == 'Blitz':
            if random.randint(0,100) <= chanceManualBlitz:                # ManualBlitz passed the asteroid belt
                print('You begin passing the asteroids one by one.')
                time.sleep(2)
                print('They are close, you can extend your hand to them.')
                time.sleep(2)
                print('As the asteroids flew by, you notice the path has been cleared.')
                time.sleep(2)
                print('You passed the asteroid belt.')
                
            else:                                                        # ManualBlitz failed to pass the asteroid belt
                print('While you were going through the asteroids...')
                time.sleep(2)
                print('"BOOM"')
                time.sleep(1)
                print('The ship\'s main reactor has been hit by a nearby asteroid and caused a fire.')
                time.sleep(3)
                print('As the fire comes closer to you, you realize that this is the end.')
                time.sleep(3)
                print('ASTEROID ENDING.')
                time.sleep(2)
                exit()
                
    if AsteroidQuestion == 2:                                      # Go around manually
        print('You went around the asteroid belt. (-30 Fuel)')
        time.sleep(1)
        print('Fuel = 60')
        Fuel = 60

time.sleep(2)
print('You can see the asteroid belt behind you. The danger is gone.')           # Passed the asteroid belt
time.sleep(2)
print('You think to yourself:')
time.sleep(1)
print('"All this risk taking and life threathening dangers for this negligible job. Fucking hell."')
time.sleep(3)
print('You continue your journey to Neptune.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('"Approaching Jupiter."')                             # Jupiter
time.sleep(2)
print('Beneath you gleams Jupiter with all it\'s glory.')
time.sleep(2)
print('"How beautiful...", you think.')
time.sleep(2)
print('As the ship sails by, Jupiter looks smaller and smaller.')
time.sleep(2)
print('This journey has been, to say the least, exhausting.')
time.sleep(2)
print('You begin to yawn and your eyes start to close.')
time.sleep(2)
print('This..')
time.sleep(2)
print('Thi..')
time.sleep(2)
print('zzzz')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print("ALERT! ALERT!")
time.sleep(2)
print('You immediately wake up.')
time.sleep(2)
print('"ALERT! ALERT! The ship is being pulled by the gravitational force of Uranus!"')
time.sleep(1.5)
print('1) ' + 'Activate the backup generators and route full power to thrusters. (-40 Fuel)')
time.sleep(1.5)
print('2) ' + 'Wait and see what happens.')

Uranus = int(input())

if Uranus == 2:                                  # Satellite
    time.sleep(1)
    print('You let the force pull the ship.')
    time.sleep(2)
    print('As you are waiting to crash onto Uranus\' surface, you realize the ship is not falling.')
    time.sleep(3)
    print('You curiously look around and notice that...')
    time.sleep(2)
    print('The ship is orbiting around Uranus!')
    time.sleep(1.5)
    print('SATELLITE ENDING')
    time.sleep(1)
    print('Achievement unlocked : The Satellite.')
    
elif Uranus == 1:                                     # Saved from Uranus
    print('You activated the backup generators')
    time.sleep(2)
    print('"Routing full power to thrusters!"')
    time.sleep(2)
    print('You feel the force pulling the ship down.')
    time.sleep(2)
    print('It\'s going to be close.')
    time.sleep(2)
    print('"ALERT! ALERT!"')
    time.sleep(1)
    print('The ship is under enormous force but it\'s resisting it. Constant vibrations arise from all parts of the ship.')
    time.sleep(3)
    print('"ALERT! ALERT!"')
    time.sleep(1)
    print('"COME ON YOU BLOODY PILE OF METAL, GET US OUT OF HERE!"')
    time.sleep(3)
    print('Silence.')
    time.sleep(2)
    print('The ship managed to pull itself away from the gravitational force of Uranus.')
    time.sleep(2)
    print('"HOLY SHIT, That was close!"')
    time.sleep(2)
    print('"I SWEAR IF THEY EVER TRANSFER ME AGAIN..."')
    time.sleep(2)
    print('And the journey continues...')
    time.sleep(3)
    print('"Approaching Neptune."')
    time.sleep(2)
    print('"Finally arriving at this god forsaken planet."')
    time.sleep(2)
    print('You take control of the ship and manually cruise it into the company\'s base.')
    time.sleep(3)
    print('You park ' + mySpaceship + ' on one of the parking slots and hop out.')
    time.sleep(2)
    print('As you are starting to walk, a man approaches you.')
    time.sleep(2)
    print('"Hey ' + myName + ', good to see you."')
    time.sleep(2)
    print('"I wish there would be another way but...')
    time.sleep(2)
    print('You become intrigued.')
    time.sleep(2)
    print('...our crew here have already studied the gas while you were gone so the company requested your transfer back to Earth..."')
    time.sleep(4)
    print('...')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('"..' + myName + '?"')
    time.sleep(2)
    print('"YOU MOTHERF..."')
    time.sleep(1)
    print('ENRAGED ENDING')
    time.sleep(1)
    print('New achievement unlocked : The Angry One.')
    

        
        























