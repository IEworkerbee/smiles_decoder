from Atom import Atom
from typing import List, Self

class Mol:
    def __init__(self, smiles: str = None):
        self.smiles = None
        self.bonds = [List[int, int]]
        self.atoms = [Atom]
        
    def copy_mol(self) -> Self:
        """
            Returns reference to a new Mol object with copied data from self

            Usage: Mol_Copy = Mol_1.copy_mol()
        """
        new_mol = Mol()
        new_mol.smiles = self.smiles
        new_mol.bonds  = self.bonds
        new_mol.atoms  = self.atoms
        return new_mol
        
    def parse_smiles(self, smiles: str = None) -> Self:
        # TODO:
        pass

    def calc_2D(self):
        # TODO: 
        pass

    # Combines self molecule with second molecule. Adds one bond to connect them. 
    def combine_mol(self, Mol_2: Self, atom_1_index: int, atom_2_index: int, bond_level: int):
        """
            param 1: Second Molecule to combine
            param 2: index of atom in first molecule to connect to second molecule
            param 3: index of atom in second molecule to connect to first molecule
            return: combined Mol object

            usage: Mol_1.combine_mol(Mol_2)
        """
        combined_mol = self.copy_mol(self)

        # offsets indexes and bond indexes of all atoms in Mol_2
        offset = len(self.atoms)
        for atom in Mol_2.atoms:
            atom.index += offset
        for bond in Mol_2.bonds:
            bond[0] += offset
            bond[1] += offset

        combined_mol.atoms.extend(Mol_2.atoms)
        combined_mol.bonds.extend(Mol_2.bonds)
        combined_mol.smiles = None

        indexes = [atom_1_index, atom_2_index]
        combined_mol.bonds.append(min(indexes), max(indexes))
        for i in indexes:
            combined_mol[i].bonds.append(bond_level)
            combined_mol[i].num_bonds += 1
            combined_mol[i].num_valence -= bond_level
            combined_mol[i].free_electron_pairs = combined_mol[i].num_valence / 2
 
        return combined_mol
    
    def add_atom(self, atom: Atom, index_atom_to_bond: int, bond_level) -> None:
            self.atoms.append(atom)
            index_new = len(self.atoms)
            self.atoms[index_new].index = index_new
            indexes = [index_new, index_atom_to_bond]
            self.bonds.append((min(indexes), max(indexes)))

            for i in indexes: 
                self.atoms[i].bonds.append(bond_level)
                self.atoms[i].num_bonds += 1
                self.atoms[i].num_valence -= bond_level
                self.atoms[i].free_electron_pairs = self.atoms[i].num_valence / 2

    def add_bond(self, index_1: int, index_2: int, bond_level: int) -> None:
        # TODO
        pass

    def add_implied_hydrogens(self):
        # GODDAMN FUCKING CARBENES
        for atom in self.atoms:
            if atom.element == 'C':
                if atom.charge == -2:
                    # carbene
                    pass
                else:
                    while atom.num_valence != 0:
                        hydrogen = Atom('H', 0)
                        self.add_atom(hydrogen)

    