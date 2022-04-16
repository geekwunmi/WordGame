import sys, time
from random import randint

class scene(object):
    
    def enter(self):
        exit(1)
        
class shonen(scene): #Not fininshed

    def enter(self):
        print ("You begin your journey in a shonen world")
        print ("Everything feels strange but familiar")
        print ("You run into your eternal rival")
        print ("You hear constant thumping while your rival charges at you")
        print ("In a split second it comes to you")
        print ("The thumping noise was coming from your heart")
        print ("You realise you're in the middle of a tournament")
       # Needs combat system (dodge, block, attack)
       
class seinen(scene):

    def enter(self):
        print ("You then transfer to a seinen world")
        print ("The earth beneath you feels limited")
        print ("A vaguely familiar voice faintly calls out to you")
        print ('"...what...is...ser..."')
        print ('It becomes much clearer after the third scream "What is your answer?"')
        print ("You realize youre on top of skyscraper looking back at your rival")
        print ("They're in the same postion, and you watch as they repeat themselves")
        print ("What could prevent but also enable a man to become God?")
        
        options = ["Himself", "Power", "Ego", "Pain"]
        
        print (options)
        
        answer = input("> ")
            
        if answer == options[0]:
            print ("A man is but a container for something greater than the self")
            
            return 'seinen'
            
        elif answer == options[1]:
            print ("A tool is only as good as the handler")
            print ("To abandon the handler and focus on the tool leads to destruction")
            
            return 'seinen'
            
        elif answer == options[2]:
            print ("Your rival smirks staring at you as they slowly close their eyes")
            print ('He shouts out "You are coreect! Join me in EgoDeath!"')
            
            return 'harem'
            
        elif answer == options [3]:
            print ("Hardship does not define men but help them to define themselves")
            
            return 'seinen'
            
        else:
            print ("Society has lied, no one is beyond conformity, choose your answer")
            
            return 'seinen'

class harem(scene):
    pass
    
            
        
        