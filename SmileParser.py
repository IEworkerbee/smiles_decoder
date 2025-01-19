from Atom import Atom



# ANDY LOOK HERE !!!!!!!!!!!!!!!!!!!!!!!
# I am going to comment this out for now.
# I think we need the H's because they are important for generating the 3D position data. 
# If we don't generate the 3D data and store it in the H atoms, then we can't do cool training with it. 
# Plus a lot of the beginning chems just look like one atom. 

# SWITCHING TO 2D
"""
def removeMostH(smile):
    index = 0

    while index < len(smile): #not working my badddddddddddd
        print('look ma im in the loop', index)
        if smile[index] == 'H':
            if (index < len(smile) - 1) & (smile[index + 1] == 'H'):
                pass
            elif (index != 0) & (smile[index - 1] == 'H'):
                pass
            else:
                smile.replace(smile[index], '')
                print("deleting the h")
        index += 1

    return smile
"""

class SmileParser():
    
    def __init__(self):
        pass

    def parse_smile(self, smiles: str):
        pass

    ##### Helpers #####

