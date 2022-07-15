'''
A robot that is not on the table can choose to ignore
the MOVE, LEFT, RIGHT and REPORT commands.
Input can be from a file, or from standard input, as the developer chooses.
'''

from constants import KEYWORDS
from constants import DIRECTIONS

def get_place_args(command: str) -> tuple:
    parameters = command.split(',')
    x = int(parameters[0])
    y = int(parameters[1])
    direction = parameters[2]
    return (x,y) , direction


def parse_input(command: str) -> tuple:
    keyword = command.split(' ')[0]
    position = None
    direction = None
    if keyword not in KEYWORDS:
        keyword = False
    if keyword == 'PLACE':
        place_parameters = get_place_args(command[6:])
        position = place_parameters[0]
        direction = place_parameters[1]
        if direction not in DIRECTIONS:
            keyword = False
    return keyword, position, direction
