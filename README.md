# Toy Robot Code Challenge

## Description and requirements:
The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.

Create a console application that can read in commands of the following form -
```
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
```
PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0) can be considered to be the SOUTH WEST most corner. It is required that the first command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed. MOVE will move the toy robot one unit forward in the direction it is currently facing.
LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot. REPORT will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient. A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands. Input can be from a file, or from standard input, as the developer chooses.
Provide test data to exercise the application.
It is not required to provide any graphical output showing the movement of the toy robot.
The application should handle error states appropriately and be robust to user input.

## Constraints

The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot. Any move that would cause the robot to fall must be ignored.

### Example Input and Output:


```

a)----------------
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH
```

```
b)----------------
PLACE 0,0,NORTH
LEFT
REPORT
Output: 0,0,WEST
```

```
c)----------------
PLACE 1,2,EAST
MOVE
MOVE
LEFT
```


## Run 

### Option 1 - Local machine
1. Download and install Python 3 [here](https://www.python.org/downloads)
2. Download the repository
3. Extract the downloaded zip file
4. Open folder `iress-toy-robot-code-challenge/` in Terminal or Command Prompt
5. Run the simualtion by running the following script
```bash
python src/game.py 
```

### Option 2 - Remote Container
1. Download and install Docker Desktop [here](https://www.docker.com/products/docker-desktop)
2. Download Visual Studio Code [here](https://code.visualstudio.com/download)
3. Download the repository
4. Extract the downloaded zip file
5. Open folder `iress-toy-robot-code-challenge/` in Visual Studio Code
6. Open project in Dev Container: click the green button in the bottom left corner of VS Code
7. Run the simualtion by running the following script in Workspace Terminal
```bash
python src/game.py 
```
or Run set of commands from file using the following script.
```bash
python src/game.py src/commands.txt 
```

## Example
```
python src/game.py 
PLACE 0,0,EAST
MOVE
MOVE
LEFT
REPORT
Output: 2,0,NORTH
MOVE
MOVE
RIGHT
REPORT
Output: 2,2,EAST
```

```
python src/game.py src/commands.txt 
PLACE 0,0,EAST
MOVE
MOVE
LEFT
REPORT
Output: 2,0,NORTH
```

Terminate the application by doing `Ctrl + Z`



## Test Case

Initiate the test case by running the following script in Workspace Terminal
```bash
pytest tests/
```

