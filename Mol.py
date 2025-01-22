from Atom import Atom
from typing import List

class Mol:
    def __init__(self, smiles: str):
        self.smiles = smiles
        self.bonds = [List[int, int]]
        self.atoms = [Atom]
        
        
    def parse_smiles(self):
        # TODO:
        pass

    def calc_2D(self):
        for atom in self.atoms:
            if atom.index == 0:
                atom.offset == 0