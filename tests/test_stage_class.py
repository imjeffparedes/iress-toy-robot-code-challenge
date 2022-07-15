'''
    Test the functions of Stage Class
'''

import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../src"))
from stage import Stage


class TestStageClass():
    stage = Stage()

    def test_is_out_of_boundaries_false(self):
        result = self.stage.is_out_of_boundaries((0,0))
        assert result == False

    def test_is_out_of_boundaries_true(self):
        result = self.stage.is_out_of_boundaries((0,6))
        assert result == True

    def test_place(self):
        position = (0,0)
        direction = 'EAST'
        result = self.stage.place(position, direction)
        assert result == (position, direction)

    def test_go_north(self):
        expected_result = 'NORTH'
        actual_result = self.stage.left()
        assert actual_result == expected_result

    def test_go_west(self):
        expected_result = 'WEST'
        actual_result = self.stage.left()
        assert actual_result == expected_result

    def test_go_south(self):
        expected_result = 'SOUTH'
        actual_result = self.stage.left()
        assert actual_result == expected_result

    def test_go_east(self):
        expected_result = 'EAST'
        actual_result = self.stage.left()
        assert actual_result == expected_result

    def test_report(self):
        expected_result = 'Output: 0,0,EAST'
        actual_result = self.stage.report()
        assert actual_result == expected_result

    def test_move_x(self):
        expected_result = (1,0)
        actual_result = self.stage.move()
        assert actual_result == expected_result

    def test_move_y(self):
        expected_result = (1,1)
        # move NORTH
        self.stage.left()
        actual_result = self.stage.move()
        assert actual_result == expected_result

    def test_right(self):
        # move EAST
        self.stage.right()
        expected_result = 'Output: 1,1,EAST'
        actual_result = self.stage.report()
        assert actual_result == expected_result
