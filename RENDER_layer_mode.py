from ursina import *
from RENDER_minefield_rendering import get_list, cubes

cubes = cubes
mine_list = list(get_list())


def proper_list():
    for i in range(len(mine_list)):
        if mine_list[i][1] != 1:
            mine_list.remove(mine_list[i])
    return mine_list


print(len(mine_list))