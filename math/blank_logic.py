#####NEEDS TO:
##take in a coordinate and return:
## connected blanks
## numbers adjacent to these blanks
## as a dictionary of coordinate:number

DEBUG = True
from minefield_logic import adjacent_finder, logical_minefield_dict_maker

if DEBUG == True:
    minefield_dict = logical_minefield_dict_maker(5, 5, 5)

def blank_chain_revealer(minefield_dict:dict, clicked_coord:tuple)->dict:
    """takes in a minefield dict and a coordinate and returns connected blanks.
        also returns numbers adjacent to these blanks"""

    
    adjacents = set(adjacent_finder(clicked_coord, (4,4,4)))
    chain_adjacents = set([])

    ##Find adjacent blanks##
    for coord in adjacents.copy():
        if minefield_dict.get(coord) == 0 and coord not in chain_adjacents:
            adjacents.update(adjacent_finder(coord, (4,4,4)))
        chain_adjacents.add(coord)


    return chain_adjacents


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