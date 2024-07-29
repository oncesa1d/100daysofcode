print('''
    *******************************************************************************
                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              Said
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

    *******************************************************************************
    ''')
print("Welcome to Treasure Island. \n Your mission is to find the treasure.")

choice1 = input("You're in a dark forest and you can't see. Which way do you want to go? left or right?").lower()

if choice1 == "left":
    choice2 = input('You\'ve come to the big lake. Write "wait" for the boat to cross or write "swim" without waiting for the boat.').lower()
    if choice2 == "wait":
        choice3 = input("You waited patiently and the kind merchants took you across in their boats. You walked and walked and three doors appeared before you. The doors are red, yellow and blue. Write the name of the door of your choice.").lower()
        if choice3 == "red":
            print("You walked into a room full of fire. Game over")
        elif choice3 == "yellow":
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Said]
*******************************************************************************
 ''')
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You walked into a room full of monsters. Game over")
        else:
            print("You chose a door that does not exist. Game over.")
    else:
        print("Oh no! Pirates found you and looted you. Game over.")
else:
    print("You hurt your leg falling into a big hole. Game over.")
