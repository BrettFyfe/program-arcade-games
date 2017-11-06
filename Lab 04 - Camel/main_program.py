#CAMEL GAME
import random
done = 1


milestraveled = 0
thirst = 0
cameltiredness = 0
drinks = 4
nativedistance = 0
nativecaught = (milestraveled - nativedistance) - 20


print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down!')
print('Survive your desert trek and outrun the natives.')

while done == 1:
    print("A. Drink from your canteen")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop and rest.")
    print("E. Status check.")
    print("Q. quit.")
    userinp = input('Your choice?: ')
    if thirst >= 4 and thirst < 6:
        print('You are thirsty.')
    if thirst >= 6:
        print('You died of thirst!')
        done = done + 1
    if cameltiredness >= 5 and cameltiredness < 8:
        print('Your camel is getting tired.')
    if cameltiredness > 8:
        print('Your camel died.')
        done = done + 1
    if nativecaught >= -15:
        print('The Natives are getting close!')
    if nativecaught >= 0:
        print('The natives have caught you.')
        done = done + 1
    if userinp == "Q": 
        done = done + 1
    if milestraveled >= 200: 
        print('You WIN! Congrats!')
        done = done + 1
    elif userinp == "E":
        print("Miles traveled: " + str(milestraveled))
        print("Drinks in canteen : " + str(drinks))
        print("The natives are " + str(abs(nativecaught)) + " miles behind you.")
    elif userinp == "D":
        cameltiredness = 0
        nativedistance = nativedistance + random.randrange(7,14)
        print('The Camel is happy.')
    elif userinp == "C":
        milestraveled = milestraveled + random.randrange(10,20)
        print("You have traveled " + (milestraveled))
        thirst = thirst + 1
        cameltiredness = cameltiredness + random.randrange(1,3)
        nativedistance = nativedistance + random.randrange(7,14)
    elif userinp == "B":
        milestraveled = milestraveled + random.randrange(5,12)
        print("You have traveled " + (milestraveled))
        thirst = thirst + 1
        nativedistance = nativedistance + random.randrange(7,14)
    elif userinp == "A":
        if drinks > 0:
            drinks = drinks - 1
            thirst = 0
            print(nativedistance)
        else:
            print('No drinks left.')
    
    
    
