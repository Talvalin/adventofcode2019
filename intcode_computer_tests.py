import unittest
import intcode_computer as IntcodeComputer


class IntCode_Computer_Tests(unittest.TestCase):

    def setUp(self):
        self.intcode_computer = IntcodeComputer.IntcodeComputer(debug=False)

    def test_opcode(self):
        opcode = self.intcode_computer.process_opcode(1002)
        self.assertEqual(opcode[0], 2)

    def test_parameter_modes(self):
        opcode = self.intcode_computer.process_opcode(1002)
        self.assertEqual(opcode[1], [0, 1, 0])

    def test_program1(self):
        self.intcode_computer.intcode = [3,0,4,0,99]
        self.intcode_computer.input = [10249]
        self.assertEqual(self.intcode_computer.execute(), 10249)

    def test_opcode8_position_mode(self):
        self.intcode_computer.intcode = [3,9,8,9,10,9,4,9,99,-1,8]
        self.intcode_computer.input = [8]
        self.assertEqual(self.intcode_computer.execute(), 1)

    def test_opcode7_position_mode(self):
        self.intcode_computer.intcode = [3,9,7,9,10,9,4,9,99,-1,8]
        self.intcode_computer.input = [8]
        self.assertEqual(self.intcode_computer.execute(), 0)

    def test_opcode8_immediate_mode(self):
        self.intcode_computer.intcode = [3,3,1108,-1,8,3,4,3,99]
        self.intcode_computer.input = [8]
        self.assertEqual(self.intcode_computer.execute(), 1)

    def test_opcode7_immediate_mode(self):
        self.intcode_computer.intcode = [3,3,1107,-1,8,3,4,3,99]
        self.intcode_computer.input = [8]
        self.assertEqual(self.intcode_computer.execute(), 0)

    def test_jump_test_position_mode_zeroinput(self):
        self.intcode_computer.intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        self.intcode_computer.input = [0]
        self.assertEqual(self.intcode_computer.execute(), 0)

    def test_jump_test_position_mode_nonzeroinput(self):
        self.intcode_computer.intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        self.intcode_computer.input = [2]
        self.assertEqual(self.intcode_computer.execute(), 1)

    def test_jump_test_immediate_mode_zeroinput(self):
        self.intcode_computer.intcode = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        self.intcode_computer.input = [0]
        self.assertEqual(self.intcode_computer.execute(), 0)

    def test_jump_test_immediate_mode_nonzeroinput(self):
        self.intcode_computer.intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        self.intcode_computer.input = [3]
        self.assertEqual(self.intcode_computer.execute(), 1)

    def test_long_example_below8(self):
        self.intcode_computer.intcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        self.intcode_computer.input = [7]
        self.assertEqual(self.intcode_computer.execute(), 999)

    def test_long_example_equals8(self):
        self.intcode_computer.intcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        self.intcode_computer.input = [8]
        self.assertEqual(self.intcode_computer.execute(), 1000)

    def test_long_example_above8(self):
        self.intcode_computer.intcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        self.intcode_computer.input = [9]
        self.assertEqual(self.intcode_computer.execute(), 1001)


if __name__ == "__main__":
    unittest.main()