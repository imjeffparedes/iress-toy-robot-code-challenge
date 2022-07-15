'''
The application is a simulation of a toy robot moving on a square table top
'''
from constants import KEYWORDS
from constants import DIRECTIONS
from constants import TABLE_DIMENSIONS


class Stage:
    ''' Simulate stage or square table top
    '''
    def __init__(self) -> None:
        '''Initiate needed parameters'''
        self.current_direction = 'NORTH'
        self.current_position = (0, 0)
        self.target_position = (0, 0)
        self.placed = False


    @staticmethod
    def is_out_of_boundaries(position: tuple) -> bool:
        '''Any movement that would result in the robot falling from the table
        must be prevented, however further valid movement commands must still be allowed.
        '''
        x = position[0]
        y = position[1]
        table_width = TABLE_DIMENSIONS[0]
        table_height = TABLE_DIMENSIONS[1]
        if (x < 0 or x > table_height) or (y < 0 or y > table_width):
            return True
        return False


    def place(self, position: tuple, direction: str) -> tuple:
        '''PLACE will put the toy robot on the table in position X,Y
        and facing NORTH, SOUTH, EAST or WEST.
        '''
        if self.is_out_of_boundaries(position):
            return
        self.current_position = position
        self.current_direction = direction
        self.placed = True
        return position, direction


    def move(self) -> tuple:
        '''MOVE will move the toy robot one unit
        forward in the direction it is currently facing.'''
        if self.placed is False:
            return

        x = self.current_position[0]
        y = self.current_position[1]

        if self.current_direction == 'NORTH':
            y+=1
        elif self.current_direction == 'SOUTH':
            y-=1
        elif self.current_direction == 'EAST':
            x+=1
        elif self.current_direction == 'WEST':
            x-=1
        new_position = (x, y)

        if self.is_out_of_boundaries(new_position):
            return self.current_position

        self.current_position = new_position

        return new_position


    def left(self)->str:
        '''LEFT will rotate the robot 90 degrees in the specified direction
        without changing the position of the robot.'''
        if self.placed is False:
            return

        direction_index = DIRECTIONS.index(self.current_direction)
        new_direction_index = direction_index - 1

        if new_direction_index < 0:
            new_direction_index = 3

        new_direction = DIRECTIONS[new_direction_index]
        self.current_direction = new_direction

        return new_direction


    def right(self)->str:
        '''RIGHT will rotate the robot 90 degrees in the specified direction
        without changing the position of the robot.'''
        if self.placed is False:
            return

        direction_index = DIRECTIONS.index(self.current_direction)
        new_direction_index = direction_index + 1

        if new_direction_index > 3:
            new_direction_index = 0

        new_direction = DIRECTIONS[new_direction_index]
        self.current_direction = new_direction

        return new_direction


    def report(self)->str:
        '''REPORT will announce the X,Y and F of the robot.
        This can be in any form, but standard output is sufficient. '''
        if self.placed is False:
            return

        x = self.current_position[0]
        y = self.current_position[1]

        result = f'Output: {x},{y},{self.current_direction}'
        print(result)

        return result
