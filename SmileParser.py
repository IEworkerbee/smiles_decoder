from Atom import Atom, element_dic
import re

validBondOperators = {'#': 3, '=': 2, '-': 1}
validCharges = {"[+]": 1, "[-]": -1}
listOfAtoms = []


class SmileParser():

    def __init__(self):
        pass

    def parse_smile(self, smiles: str):
        pass


# first step is adding in all of the implied single bonds. let's break it up based on capitalization

def addImpliedSingleBonds(smile: str):
    # NOTE: this might become a problem with aromatic ring representation, so be aware of that!
    # might have to figure out a way to ONLY look at elements instead of breaking by capital letters
    breaking = re.findall(r'[A-Z][^A-Z]*|"[+]"|"[-]"| [(]', smile)

    # i know this isn't a great solution i just don't know how regex works rn
    breaking = ' - '.join(breaking)
    breaking = breaking.replace(' - =', '=')
    breaking = breaking.replace('= - ', '=')
    breaking = breaking.replace(' - #', '#')
    breaking = breaking.replace('# - ', '#')

    print(breaking)

    return breaking


def parseBranch(smile: str):
    smile = addImpliedSingleBonds(smile)
    splitSmile = re.split(r'( - |=|#)', smile)

    i = 0
    while i < len(splitSmile):
        # sort either element or bond
        # if element then make a new atom object
        if any(el in splitSmile[i] for el in element_dic):

            # check charges
            element = splitSmile[i].strip("[+][-]")
            charge = 1 if "[+]" in splitSmile[i] else -1 if "[-]" in splitSmile[i] else 0
            # print("\tELEMENT-> ", element, " CHARGE-> ", charge)

            newAtom = Atom(element, [], False, charge, i)
            if not i == 0:
                # add in your bonds babyyyyyyy
                lastBond = splitSmile[i - 1]

                # NOTE TO SELF: put this in a seperate function to call
                lastBond = lastBond.replace(" ", "")
                bond = 1 if lastBond in "-" else 2 if lastBond in "=" else 3
                newAtom.bonds.append(bond)

            listOfAtoms.append(newAtom)

        elif any(bond in splitSmile[i] for bond in validBondOperators):
            split = splitSmile[i].replace(" ", "")
            bond = 1 if split in "-" else 2 if split in "=" else 3

            listOfAtoms[-1].bonds.append(bond)

        i = i + 1

    for ex in listOfAtoms:
        print(ex.element, " ", ex.bonds)

    return listOfAtoms[-1]


def traverse(smile: str):
    print("got string", smile)
    # need to add nested loop functionality
    if "(" in smile or ")" in smile:
        print("------>found () ")
        traverse((smile.split('('))[1].split(')')[0])
    else:
        parseBranch(smile)

    # parseBranch(smile)


# goThroughBranches("CCCHe(O[+]C=C)C")
# parseBranch("CC#C=HeO[+]C[-]C")
traverse("CCC(CCOHe)CC=O(O(Br))")
print("what's uppppp")