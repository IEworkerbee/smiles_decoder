from Atom import Atom
from math import cos, sin, pi, sqrt

def get_position(origin: Atom, atom_to_fill: Atom):
    offset = origin.offset
    angle = origin.get_angle_type()
    length = (origin.covalent_radii + atom_to_fill.covalent_radii)
    new_position = (None, None)
    if origin.orientation == 'UP':
        atom_to_fill.offset = offset - (angle - 180)
        atom_to_fill.orientation = 'DOWN'
    else:
        atom_to_fill.offset = offset + (angle - 180)
        atom_to_fill.orientation = 'UP'
    
    x = length * cos(atom_to_fill.offset)
    y = length * sin(atom_to_fill.offset)

    new_position[0] = x
    new_position[1] = y

    


		
    

    