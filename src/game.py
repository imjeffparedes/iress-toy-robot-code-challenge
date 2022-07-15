'''
The application is a simulation of a toy robot moving on a square table top
'''
import sys
from stage import Stage
from command_parser import parse_input


stage = Stage()


def process_input(parameters: tuple):
    keyword = parameters[0]
    if keyword == 'PLACE':
        position = parameters[1]
        direction = parameters[2]
        stage.place(position, direction)
    elif stage.placed is False:
        return
    elif keyword == 'MOVE':
        stage.move()
    elif keyword == 'LEFT':
        stage.left()
    elif keyword == 'RIGHT':
        stage.right()
    elif keyword == 'REPORT':
        stage.report()


def read_file_input():
    '''Read all commands per line
    '''
    try:
        with open(sys.argv[1], 'r') as lines:
            for command in lines:
                command = command.strip().rstrip()
                print(command)
                parameters = parse_input(command)
                process_input(parameters)
    except Exception:
        return


def read_standard_input():
    try:
        while True:
            command = input().strip()
            parameters = parse_input(command)
            process_input(parameters)
    except Exception:
        read_standard_input()


## MAIN APPLICATION
if __name__ == '__main__':
    if len(sys.argv) != 1:
        read_file_input()
    else:
        read_standard_input()
