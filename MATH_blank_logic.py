#Desc: makes a function which provides coordinates which are chained together, and their values in a dict

DEBUG = False
from MATH_minefield_logic import adjacent_finder, logical_minefield_dict_maker

if DEBUG == True:
    minefield_dict = logical_minefield_dict_maker(5, 5, 5)

def blank_chain_revealer(minefield_dict:dict, clicked_coord:tuple)->dict:
    """takes in a minefield dict and a coordinate and returns connected blanks.
        also returns numbers adjacent to these blanks"""

    
    adjacents = set(adjacent_finder(clicked_coord, (4,4,4)))
    chain_adjacents = set([])
    chain_dict = {}

    ##Find adjacent blanks##
    for coord in adjacents.copy():
        if minefield_dict.get(coord) == 0 and coord not in chain_adjacents:
            adjacents.update(adjacent_finder(coord, (4,4,4)))
        chain_adjacents.add(coord)

    for coord in chain_adjacents:
        chain_dict.update({coord:minefield_dict.get(coord)})

    return chain_dict


if DEBUG == True:
    for coord in minefield_dict:
        if minefield_dict.get(coord) == 0:
            clicked_coord = coord
    
    if minefield_dict.get(clicked_coord) == 0:
        print(blank_chain_revealer(minefield_dict, clicked_coord))
"""
implement like:
if minefield_dict.get(clicked_coord) == 0:
    var = blank_chain_revealer(minefield_dict, clicked_coord)
"""