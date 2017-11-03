#3.1 Lab quiz
totalcorrect= 0
inpanswer = "if statements"
inp2answer = "print statements"
inp3answer = "1600"
inp4answer = "6AM"
inp5answer = "CSD"

inp = input('how do you check multiple conditions at once?: ')
if inp == inpanswer:
    print('Good job!')
    totalcorrect = totalcorrect + 1
else:
    print('wrong.')

inp2 = input('how do you print things?: ')
if inp2 == inp2answer:
    print('Good job!')
    totalcorrect = totalcorrect + 1
    
else:
    print('wrong.')
    
inp3 = input('What is 40*40?: ')
if inp3 == inp3answer:
    print('Good job!')
    totalcorrect = totalcorrect + 1

else:
    print('wrong.')
    
inp4 = input('What time is a little absurd to wake up in the morning?: ')
if inp4 == inp4answer:
    print('Yup, thats the time.')
    totalcorrect = totalcorrect + 1
    
else:
    print('nope. wrong.')
    
inp5 = input('What class is this for?: ')
if inp5 == inp5answer:
    print('yup, lel.')
    totalcorrect = totalcorrect + 1
    
else:
    print('wrong.')
    
print("you got" + " " + str(totalcorrect) + " " + "answers right!")
