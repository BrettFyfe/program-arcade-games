#Complete part 2
Number = int(input('n: '))
OSRow = (int(Number)*2 * 'o')
OSSpace= int(Number) - 1
OSS = (int(Number) - 2)
OSCol = (OSS * 'o')

for row in range(1):
    print(OSRow)
    for column in range(OSS):
        print('o' + 2*OSSpace * " " + 'o')
        
print(OSRow)
