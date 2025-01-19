from Atom import Atom, element_dic
import re
from geometry import get_position

validBondOperators = {'#': 3, '=': 2, '-': 1}
validCharges = {"[+]": 1, "[-]": -1}
listOfElements = []


# ANDY LOOK HERE !!!!!!!!!!!!!!!!!!!!!!!
# I am going to comment this out for now.
# I think we need the H's because they are important for generating the 3D position data. 
# If we don't generate the 3D data and store it in the H atoms, then we can't do cool training with it. 
# Plus a lot of the beginning chems just look like one atom. 

# # SWITCHING TO 2D
# def removeMostH(smile):
#     index = 0
#
#     while index < len(smile): #not working my badddddddddddd
#         print('look ma im in the loop', index)
#         if smile[index] == 'H':
#             if (index < (len(smile) - 2)) & (smile[index + 1] == 'H'):
#                 pass
#             elif (index != 0) & (smile[index - 1] == 'H'):
#                 pass
#             else:
#                 smile.replace(smile[index], '')
#                 print("deleting the h")
#         index += 1
#
#     return smile


class SmileParser():
    
    def __init__(self):
        pass

    def parse_smile(self, smiles: str):
        pass


def parseSmileSeg(smile: str):
    isTwoEl = False
    skipCharges = 0
    lastCharge = 0
    lastBond = 1

    for i, char in enumerate(smile):
        if isTwoEl:
            isTwoEl = False
            continue

        if skipCharges != 0:
            skipCharges -= 1
            continue

        if (i + 3) < (len(smile)-1):
            nextThree = char + "" + smile[i+1] + "" + smile[i+2]
            if nextThree in validCharges:
                if (i == 0):
                    raise ValueError("That charge can't be there")
                else:
                    lastCharge = validCharges[nextThree]
                    print(lastCharge, " CHARGE FOUND!")
                    skipCharges = 3
                    continue

        # check the string
        currentElement = char
        if (i < (len(smile) - 2)):
            if (smile[i+1].islower()):
                isTwoEl = True
                currentElement =  currentElement + "" + smile[i+1]

        if currentElement in element_dic:
            # make the atom
            currAtom = Atom(currentElement, [0,0], False, False, -1)
            print(currAtom.element)
            listOfElements.append(currAtom)

            currAtom.bonds.append(lastBond)
            lastBond = 1

        elif char in validBondOperators:
            print(currentElement)
            print("omg it's a valid bond operator, come back to this")

            last_element = listOfElements[-1]
            lastBond = validBondOperators[char]
            last_element.bonds.append(validBondOperators[char])

        else:
            print("GAHHH", currentElement)
            raise ValueError("Cannot read SMILE with unknown elements")

def goThroughBranches(smile):
    try:
        branch = re.match(r"(.*)\((.*)\)", smile).groups()
        parseSmileSeg("".join(branch))
    except:
        pass


    for i, element in enumerate(listOfElements):
        listOfElements[i].index = i



    ##### Helpers #####

goThroughBranches("HH[-]OH")

def test_get_position():
    atom_1 = listOfElements[0]
    atom_2 = listOfElements[1]
    atom_3 = listOfElements[2]
    atom_4 = listOfElements[3]
    get_position(atom_1, atom_2)
    get_position(atom_1, atom_3)
    get_position(atom_3, atom_4)
    print(atom_1.pos)
    print(atom_2.pos)
    print(atom_3.pos)
    print(atom_4.pos)

test_get_position()