class scene(object):

    def enter(self):
        exit(1)


class shonen(scene):

    def enter(self):
            print("You begin your journey in an action world")
            print("Everything feels strange but familiar")
            print("You run into your eternal rival")
            print("You hear constant thumping while your rival charges at you")
            print("In a split second it comes to you")
            print("The thumping noise was coming from your heart")
            print("You realise you're in the middle of a tournament")

            shonenoptions = ["Block", "Dodge", "Attack"]

            print(shonenoptions)
            print("\n ------------------------------------------- \n")

            answer = input("> ")

            if  answer.casefold() == shonenoptions[2].casefold():
                print("Your rival dodges your blow ")
                print("You receive a blow to the head")
                print("Your rival cuts through your nape while you're passed out. You lose.")
                print("\n ------------------------------------------- \n")


                return shonen(),False

            elif answer == shonenoptions[0].casefold() or answer == shonenoptions[1].casefold():
                print("You survive the first attack from your rival")
                print("You see him stagger off balance, what would be your next attack?")

                print(shonenoptions)
                print("\n ------------------------------------------- \n")

                answer2 = input("> ")

                if answer2 == shonenoptions[0].casefold() or answer2 == shonenoptions[1].casefold():
                    print("Your rival suddenly regain composure and throws dust into the air")
                    print("You were wise to see through his your rivals feint")
                    print("He makes a large swing that cuts through the dust and leaves himself unbalanced")

                    print(shonenoptions)
                    print("\n ------------------------------------------- \n")

                    answer3 = input("> ")

                    if answer3.casefold() == shonenoptions[2].casefold():
                        print("You struck down your rival!")
                        print("The colosseum roars at victory")
                        print("You're then teleported to the world of seinen")
                        print("\n ------------------------------------------- \n")

                        return seinen(),False

                    else:
                        print("Learn to seize your opportunities as they come")
                        print("\n ------------------------------------------- \n")
                        return shonen(),False

                else:
                    print("You've fallen into your rivals trickery")
                    print("Those most eager to draw blood are first to find themselves wounded")
                    print("\n ------------------------------------------- \n")

                    return shonen(),False
            else:
                print("Choose a battle option from the list of moves given")
                print("Come on! You can do this! Fight!")
                print("\n ------------------------------------------- \n")

                return shonen(),False
class seinen(scene):

    def enter(self):
        print("You then transfer to a psychological world")
        print("The earth beneath you feels limited")
        print("A vaguely familiar voice faintly calls out to you")
        print('"...what...is...ser..."')
        print('It becomes much clearer after the third scream "What is your answer?"')
        print("You realize you're on top of skyscraper looking back at your rival")
        print("They're in the same position, and you watch as they repeat themselves")
        print("What could prevent, but also enable a man to become God?")
        print("\n ------------------------------------------- \n")

        seinenoptions = ["Himself", "Power", "Ego", "Pain"]

        print(seinenoptions)

        answer4 = input("> ")

        if answer4.casefold() == seinenoptions[0].casefold():
            print("A man is but a container for something greater than the self")
            print("\n ------------------------------------------- \n")

            return seinen(),False

        elif answer4.casefold() == seinenoptions[1].casefold():
            print("A tool is only as good as the handler")
            print("To abandon the handler and focus on the tool leads to destruction")
            print("\n ------------------------------------------- \n")

            return seinen(),False

        elif answer4.casefold() == seinenoptions[2].casefold():
            print("Your rival smirks staring at you as they slowly close their eyes")
            print('He shouts out "You are correct! Join me in EgoDeath!"')
            print("\n ------------------------------------------- \n")

            return harem(),False

        elif answer4.casefold() == seinenoptions[3].casefold():
            print("Hardship does not define men; but help them to define themselves")
            print("\n ------------------------------------------- \n")

            return seinen(),False

        else:
            print("Society has lied, no one is beyond conformity, choose your answer")
            print("\n ------------------------------------------- \n")

            return seinen(),False


class harem(scene):

    def enter(self):
        print("You're teleported to the world and meet your love interests")
        print("You're welcome by a group of women your age")
        print("You need to chose which one you'd like to spend time with")
        print("\n ------------------------------------------- \n")

        haremoptions = ['Lolita', 'Childhood Friend', 'TomBoy', 'Broken Girl']

        print(haremoptions)

        answer5 = input("> ")

        if  answer5.casefold() == haremoptions[0].casefold():
            print("You're a terrible person and you should be arrested")
            print("I mean i am a Nabokov fan as well but that's illegal")
            print("and morally wrong")
            print("Just stop")
            print("\n ------------------------------------------- \n")

            return harem(),False

        elif    answer5.casefold() == haremoptions[1].casefold():
            print("You're obviously a very sentimental person.")
            print("You're childhood friend has changed greatly since last time you met")
            print("Now they do drugs and steal money")
            print("You end up being sold off into human trafficking")
            print("\n ------------------------------------------- \n")

            return harem(),False

        elif    answer5.casefold() == haremoptions[2].casefold():
            print("It is revealed to you that the tomboy is actually your rival")
            print("they only put you though all those contests because they wanted to seem interesting")
            print("Tomboys are the Answer. You win")
            print("\n ------------------------------------------- \n")

            return harem(),True

        elif    answer5.casefold() == haremoptions[3].casefold():
            print("Why do you like suffering?")
            print("Are you one of those weirdos that wants someone obsessed with them?")
            print("Get a life weirdo")
            print("\n ------------------------------------------- \n")

            return harem(),False

        else:
            print("Chose an option from the list given")
            print("\n ------------------------------------------- \n")

            print(haremoptions)

            return harem(),False


if __name__ == "__main__":
    gameisrunning = True
    currentscene = shonen()

    while gameisrunning:
        currentscene,hasgameended = currentscene.enter()
        if hasgameended == True:
            gameisrunning = False
        
        
