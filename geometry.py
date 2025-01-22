from Atom import Atom
from math import cos, sin, pi

def get_position(origin: Atom, atom_to_fill: Atom):
    offset = origin.offset
    angle = origin.get_angle_type()
    print(angle)
    origin.offset = (origin.offset + angle) % 360
    length = (origin.covalent_radii + atom_to_fill.covalent_radii)
    if origin.orientation == 'UP':
        atom_to_fill.offset = offset + angle
        atom_to_fill.orientation = 'DOWN'
    else:
        atom_to_fill.offset = offset - angle
        atom_to_fill.orientation = 'UP'
    
    print(length)
    print(atom_to_fill.offset)
    x = length * cos(atom_to_fill.offset * (pi/180))
    y = length * sin(atom_to_fill.offset * (pi/180))

    atom_to_fill.pos[0] = x + origin.pos[0]
    atom_to_fill.pos[1] = y + origin.pos[1]

def test_get_position():
    atom_1 = Atom('O', [1, 1], False, 0, 0)
    atom_2 = Atom('H', [1], False, 0, 1)
    atom_3 = Atom('H', [1, 1], False, -1, 2)
    atom_4 = Atom('H', [1], False, 0, 3)
    get_position(atom_1, atom_2)
    get_position(atom_1, atom_3)
    get_position(atom_3, atom_4)
    print(atom_1.pos)
    print(atom_2.pos)
    print(atom_3.pos)
    print(atom_4.pos)

test_get_position()
    


		
    

    