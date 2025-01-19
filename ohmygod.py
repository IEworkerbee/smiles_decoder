from abc import ABC, abstractmethod

class Atom(ABC):
    def __init__(self, ):
        pass

    @abstractmethod
    def element(self):
        pass


class Carbon(Atom):
    def __init__(self, dif_in_pref_bonds, aromatic, charge):
        self.dif_in_pref_bonds = dif_in_pref_bonds
        self.aromatic = aromatic
        self.charge = charge
    def element(self):
        return 'C'




