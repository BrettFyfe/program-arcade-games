#!usr/bin/env Python3
#Chapter 7 lab: Adventure game
#Ya Boi Brett
#11/28/17

'''First copy of adventure game from the chapter 7 lab.'''

current_room = 0
done = False
next_room = 0

room_list = []
start = ['Starting point. Passages to N, E, and W.', 6, None, 5, 1]
Restroom = ['Bathroom. Passages to N and E.', 2, None, 0, None]
HallwayA = ['HallwayA. Passages to E and S.', None, 1, 3, None]
HallwayB = ['HallwayB. Passages to W and S.', None, 5, None, 3]
Armory = ['Armory. Passages to N and W.', 4, None, None, 0]
Diningroom = ['Dining Room. Passage to S.', None, 0, None, None]
PassagetoExit = ['Passageway to finish. Passages to N, E,and W.', 7, None, 4, 3]
Exit = ['You won!', None, 3, None, None]

room_list.append(start)
room_list.append(Restroom)
room_list.append(HallwayA)
room_list.append(PassagetoExit)
room_list.append(HallwayB)
room_list.append(Armory)
room_list.append(Diningroom)
room_list.append(Exit)

while done == False:
    print()
    print(room_list[current_room][0])
    userinput = input('What do you want to do? (N, S, E, W, Quit): ')
    userinput2 = userinput.upper()
    if userinput2 == 'N':
        next_room = room_list[current_room][1]
        if next_room == None:
            print('You cant go that way.')
        else:
            current_room = next_room
    elif userinput2 == 'S':
        next_room = room_list[current_room][2]
        if next_room == None:
            print('You cant go that way.')
        else:
            current_room = next_room
    elif userinput2 == 'E':
        next_room = room_list[current_room][3]
        if next_room == None:
            print('You cant go that way.')
        else:
            current_room = next_room
    elif userinput2 == 'W':
        next_room = room_list[current_room][4]
        if next_room == None:
            print('You cant go that way')
        else:
            current_room = next_room
    elif userinput2 == 'QUIT':
        done = True        
    else:
        print('Im sorry. Your Directions are not clear. Try again.')
    if current_room == 7:
        print('Great job, you won!')
        done = True
