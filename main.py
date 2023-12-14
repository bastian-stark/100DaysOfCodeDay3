#Initiate game
print('Welcome to Treasure Island. Your Mission is to find the treasure.')

#Question 1
direction = input("You're at a crossroad. " + 'Where do you want to go? Type "left" or "right". \n')
if direction.lower() == 'right':
    print('You walked right into a group of angry (and hungry) trolls. Game over. ')
elif direction.lower() == 'left':
    #Question 2
    lakeDecision = input('You come to a lake. There is an island in the middle of the lake. Type "wait" for a boat. Type "swim" to swim across.\n')
    if lakeDecision.lower() == 'swim':
        print('Tentacles reach around your ankle and pull you under. Game over.')
    elif lakeDecision.lower() == 'wait':
        #Question 3
        doorColor = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose? \n')
        if doorColor.lower() == 'red' or doorColor.lower() == 'blue':
            print("There's an angry witch inside! You are now on fire. Game over.")
        else:
            print('You win!')