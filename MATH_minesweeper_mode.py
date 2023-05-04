#function to be used when minesweeping mode is activated
#mode will probably work by button activation causing LED to change
#based on where mine is to a given location


from MATH_minefield_logic import *
import requests
from API_PostReqs_for_PC import *
DEBUG = False

#initalize LED status on server
#requests.post(url=POST_URL, data={"value":False})

def mine_locator(minefield_dict:dict, adjacents:list, layer_number:int):
    for coord in adjacents:
        if coord in minefield_dict and minefield_dict.get(coord) == '*':
            return layer_number

    return False        #could fail, thus we need to know
    

def sweeping_mode(minefield_dict:dict, clicked_coord:tuple)->int:
    """takes dict and coordinate to find closest mine, and then turns
        that into an integer which corresponds to a LED list."""

    LED_LIST=[0,1,2,3,4] #4 is the farthest a mine can be on a 5x5x5

    #zeroth(?) ring
    if clicked_coord == "*":
        return 0

    #first ring
    first_adjacents = adjacent_finder(clicked_coord, (4,4,4))
    mine_location = mine_locator(minefield_dict, first_adjacents, 1)

    if mine_location != False:
        return mine_location
    
    #second ring
    second_adjacents = set([])
    for coord in first_adjacents:
        second_adjacents.update(adjacent_finder(coord, (4,4,4)))

    mine_location = mine_locator(minefield_dict, second_adjacents, 2)
    if mine_location != False:
        return mine_location
    
    #third ring
    third_adjacents = set([])
    for coord in second_adjacents:
        third_adjacents.update(adjacent_finder(coord, (4,4,4)))
    
    mine_location = mine_locator(minefield_dict, third_adjacents, 3)
    if mine_location != False:
        return mine_location
            


if DEBUG == True:
    minefield_dict = limited_minefield_dict(5, 5, 5)
    print(sweeping_mode(minefield_dict, (0,0,0)))
    

    
