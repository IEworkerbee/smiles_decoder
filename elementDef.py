#key is the string with the name of the chemical, value is atomic number, valence electrons
#hardcoded information about each of the elements

element_dic = {'C': 4, 'N': 5, 'O': 6, 'S': 6, 'Mg': 2, 'Br': 7, 'Si': 4, 'I': 7, 'Ca': 2, 'Ba': 2, 'Rb': 1, 'K': 1, 'Na': 1, 'Li': 1, 'H': 1, 'Al': 3, 'B': 3, 'Ne': 8, 'He': 2}

class Atom:
    def __init__(self, element, bonds, aromatic, charge):
        self.element = element
        self.bonds = bonds
        self.aromatic = aromatic
        self.charge = charge




