# makes the minefield and stores it in a dictionary of {coordinate:number of mines/ mines nearby etc.}
from random import choice
from math import floor


def coordinate_mapper(x_amount:int, y_amount:int, z_amount:int)->list:
    # the largest value will be x_amount-1, y_amount-1, z_amount-1
    # list is generated in order of z,y,x 
    return [(x, y, z) for x in range(x_amount) for y in range(y_amount) for z in range(z_amount)]

    
def minefield_dict_maker(coord_list:list)->dict:
    # all coordinates start with 0 mines because field is unpopulated
    return {coord_list[i] : 0 for i in range(len(coord_list))}


def minefield_populator(minefield_dict:dict, difficulty:int=1)->dict:
    # difficulty will be a potential addition, if so, it will use the following values
    difficulties = [0.15, 0.2, 0.25]
    # default will be 0.15, floor because no half nor 0.96 mines.
    minefield_density = floor(len(minefield_dict) * difficulties[difficulty])

    #populate the field
    chosen_spot_set = set({})   #stores previously chosen spots
    coordinate_pool = list(minefield_dict.keys())     #gets set of minefield coordinates

    while len(chosen_spot_set) <= minefield_density:   #until the appropriate amount of mines achieved

        chosen_spot = choice(coordinate_pool)     #choose from coordinates in minefield
        
        if chosen_spot in chosen_spot_set:
            continue        #break on repeats

        else:
            chosen_spot_set.add(chosen_spot)
            minefield_dict[chosen_spot] = '*'   #make spots into mines

    return minefield_dict








