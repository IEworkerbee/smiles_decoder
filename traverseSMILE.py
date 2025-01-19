from elementDef import *

def removeMostH(smile):
    index = 0

    while index < len(smile): #not working my badddddddddddd
        print('look ma im in the loop', index)
        if smile[index] == 'H':
            if (index < len(smile) - 1) & (smile[index + 1] == 'H'):
                continue
            elif (index != 0) & (smile[index - 1] == 'H'):
                continue
            else:
                smile.replace(smile[index], '')
                print("deleting the h")
        index += 1

    return smile

newString = removeMostH('CHCCCHCHHC')
print(newString)
