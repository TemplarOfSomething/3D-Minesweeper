


    #Desc: takes a minefield dictionary and implements the number logic of the field

#Imports
from minefield_maker import *

#Constants
DEBUG = False

if DEBUG == True:
    x_size = 3
    y_size = 3
    z_size = 3
    minefield_dict = minefield_populator(minefield_dict_maker(coordinate_mapper(x_size, y_size, z_size)))

def adjacent_finder(coordinate:tuple, largest_coord:tuple)->list:
    """takes a key from the minefield_dict and returns all valid adjacent spaces"""

    ##Variables to easily create ranges of what coordinates are adjacent##
    #range maxes are +2 due to uninclusive range
    x_range = [coordinate[0]-1, coordinate[0]+2]
    y_range = [coordinate[1]-1, coordinate[1]+2]
    z_range = [coordinate[2]-1, coordinate[2]+2]


    ##create the list of adjacent coords##
    adjacent_list = [(x, y, z) for x in range(x_range[0], x_range[1]) for y in range(y_range[0], y_range[1]) for z in range(z_range[0], z_range[1])]
    unfiltered_adj_list = adjacent_list     #for debug

    ##remove invalid coords##
    #invalid coords are self, negative or x,y,z greater than largest coord
    adjacent_list.remove(coordinate)
    
    adjacent_list = list(filter(lambda x: 
    0 <= x[0] <= largest_coord[0] and 
    0 <= x[1] <= largest_coord[1] and
    0 <= x[2] <= largest_coord[2], 
    adjacent_list))
 

    ##Debug##
    if DEBUG == True:
        print("Unfiltered adjacents:")
        print(*unfiltered_adj_list, sep=", ")
        print("Filtered adjacents:")
        print(*adjacent_list, sep=", ")

    return adjacent_list

def logic_implementer(coordinate:tuple, adjacent_list:list, minefield_dict:dict)->int:
    """takes a coordinate, its adjacent spaces, and updates the minefield dictionary accordingly"""
    adjacent = 0

    for i in adjacent_list:
        if minefield_dict.get(i) == '*':
            adjacent += 1
    if minefield_dict.get(coordinate) != '*':
        minefield_dict.update({coordinate:adjacent})

    if DEBUG == True:
        print(f"what was updated: {coordinate}:{adjacent}")

def logical_minefield_dict_maker(x_size:int, y_size:int, z_size:int)->dict:

    #make the logically incorrect dict
    minefield_dict = minefield_populator(minefield_dict_maker(coordinate_mapper(x_size, y_size, z_size)))

    #make it logically correct
    for i in minefield_dict:
        adjacent = adjacent_finder(i, (x_size, y_size, z_size))
        logic_implementer(i, adjacent, minefield_dict)

    return minefield_dict

if DEBUG == True:
    for i in minefield_dict:
        adjacent = adjacent_finder(i, (x_size, y_size, z_size))
        logic_implementer(i, adjacent)
    
    for i in minefield_dict:
        print(i, minefield_dict[i])