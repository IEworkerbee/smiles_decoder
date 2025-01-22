#key is the string with the name of the chemical, value is atomic number, valence electrons
#hardcoded information about each of the elements (# valence electrons, picometers atomic radii)

from typing import List

element_dic = {'C':  (4,  77), 
               'N':  (5,  75), 
               'O':  (6,  73), 
               'S':  (6,  71), 
               'Mg': (2, 130), 
               'Br': (7, 111), 
               'Si': (4, 111), 
               'I':  (7, 133), 
               'Ca': (2, 174), 
               'Ba': (2, 198), 
               'Rb': (1, 211), 
               'K':  (1, 196), 
               'Na': (1, 154), 
               'Li': (1, 134), 
               'H':  (1,  37), 
               'Al': (3, 118), 
               'B':  (3,  82), 
               'Ne': (8,  69), 
               'He': (2,  32)
               }

class Atom:
    def __init__(self, element: str, bonds: List[int], aromatic: bool, charge: int, index: int) -> bool: 
        """
        Param:
            Element:  String holding atomic symbol
            Bonds:    List of bond types connecting to element: 1, 2, 3 for bond type
            Aromatic: bool, is aromatic?
            Charge:   -1, 0, +1

            returns:  bool (success?)
        """
        self.index = index
        self.element = element
        self.bonds = bonds
        self.num_bonds = len(bonds)
        self.aromatic = aromatic
        self.charge = charge
        self.offset = 0
        self.pos = [0, 0]
        self.orientation = 'UP'
        self.num_valence         = element_dic[element][0] - sum(bonds) - (charge) 
        self.free_electron_pairs = self.num_valence / 2
        self.covalent_radii      = element_dic[element][1]

    def get_angle_type(self) -> float:
        """
            LinearLeaf       : 180   Deg
            2BondsNoPairs    : 180   Deg
            Tri3Bonds0Pairs  : 120   Deg
            Tri2Bonds1Pairs  : 120   Deg (About)
            Tetra4Bonds0Pairs: 109.5 Deg
            Tetra3Bonds1Pairs: 107   Deg
            Tetra2Bonds2Pairs: 104.5 Deg
            5Bonds           : [(0, 90, 0), (0, )  ]
        """
        if (self.num_bonds == 1):
            return 0
        
        elif (self.num_bonds == 2 and self.free_electron_pairs == 0):
            return 0
        
        elif (self.num_bonds == 3 and self.free_electron_pairs == 0):
            return 120
        
        elif (self.num_bonds == 2 and self.free_electron_pairs == 1):
            return 120 #119.9999???
        
        elif (self.num_bonds == 4 and self.free_electron_pairs == 0):
            return 109.5
        
        elif (self.num_bonds == 3 and self.free_electron_pairs == 1):
            return 107
        
        elif (self.num_bonds == 2 and self.free_electron_pairs == 2):
            return 104.5
        
        elif (self.num_bonds == 5 and self.free_electron_pairs == 0):
            return (90, 120)
        
       
    