'''
The application is a simulation of a toy robot moving on a square table top
'''

KEYWORDS = ('PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT')
DIRECTIONS = ('NORTH', 'EAST', 'SOUTH', 'WEST')
TABLE_DIMENSIONS = (5, 5)
X_DIRECTIONS = ('NORTH', 'SOUTH')
Y_DIRECTIONS = ('EAST', 'WEST')


def get_place_args(command: str) -> tuple:
    parameters = command.split(',')
    x = int(parameters[0])
    y = int(parameters[1])
    direction = parameters[2]
    return (x,y) , direction


def get_input() -> tuple:
    command = input().strip()
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


class Stage:
    ''' Simulate stage or square table top
    '''
    def __init__(self) -> None:
        '''Initiate needed parameters'''
