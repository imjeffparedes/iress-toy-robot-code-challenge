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


    @staticmethod
    def is_out_of_boundaries(position: tuple) -> bool:
        '''Any movement that would result in the robot falling from the table
        must be prevented, however further valid movement commands must still be allowed.
        '''


    def place(self, position: tuple, direction: str) -> tuple:
        '''PLACE will put the toy robot on the table in position X,Y
        and facing NORTH, SOUTH, EAST or WEST.
        '''


    def move(self) -> tuple:
        '''MOVE will move the toy robot one unit
        forward in the direction it is currently facing.'''


    def left(self)->str:
        '''LEFT will rotate the robot 90 degrees in the specified direction
        without changing the position of the robot.'''


    def right(self)->str:
        '''RIGHT will rotate the robot 90 degrees in the specified direction
        without changing the position of the robot.'''


    def report(self)->str:
        '''REPORT will announce the X,Y and F of the robot.
        This can be in any form, but standard output is sufficient. '''
