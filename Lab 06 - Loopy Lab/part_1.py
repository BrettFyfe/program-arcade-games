
x = 10 

for row in range(9):
    for column in range(row+1):
        print (x, end = " ")
        x = x + 1
        
    print()
