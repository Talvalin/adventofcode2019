import copy

status_flags = ['WORKING', 'HALTED', 'WAITING', 'ERROR']

class IntcodeComputer:
    def __init__(self, intcode=None, input=None, pointer=0, debug=False):
        self.intcode = copy.deepcopy(intcode)
        self.input = input
        self.pointer = pointer
        self.debug = debug
        self.last_output = None
        self.status = status_flags[0]
    
    def get_next_input(self):
        return self.input.pop(0)

    def get_parameter_value(self, parameter, mode):
        value = 0
        if mode == 0:
            value = self.intcode[parameter]
        elif mode == 1:
            value = parameter
        return value

    def process_opcode(self, opcode):
        # pad opcode
        opcode_array = list(str(opcode))
        if len(opcode_array) < 5:
            for _ in range(5-len(opcode_array)):
                opcode_array.insert(0, "0")

        processed_opcode = []
        processed_opcode.append(int(opcode_array[-2] + opcode_array[-1]))

        # create reversed list of parameter modes
        parameter_modes = [int(x) for x in reversed(opcode_array[0:3])]   

        # append parameters in reverse order
        processed_opcode.append(parameter_modes)
        return processed_opcode

    def execute(self):
        if self.debug:
           print("Current pointer: ", self.pointer)
        while self.status == 'WORKING':
            # get opcode
            opcode = self.process_opcode(self.intcode[self.pointer])
            self.run_instruction(opcode)

        if self.status == 'HALTED':
            return self.last_output

    def run_instruction(self, opcode):
        current_opcode = opcode[0]
        parameter1_mode = opcode[1][0]
        parameter2_mode = opcode[1][1]
        #parameter3_mode = opcode[1][2]

        if self.debug:
            print("Opcode: ", current_opcode)
            print("Current instruction pointer: ", self.pointer)
        if current_opcode == 99:
            self.status = status_flags[1]
        elif current_opcode == 3:
            # get parameter
            parameter = self.intcode[self.pointer+1]
            self.intcode[parameter] = self.get_next_input()
            self.pointer += 2
        elif current_opcode == 4:
            # get parameter
            parameter1 = self.intcode[self.pointer+1]
            parameter1_value = self.get_parameter_value(parameter1, parameter1_mode)
            self.last_output = parameter1_value
            if self.debug:
                print("Test output: ", parameter1_value)
            self.pointer += 2
        elif current_opcode == 5:
            parameter1, parameter2 = self.intcode[self.pointer+1:self.pointer+3]
            parameter1_value = self.get_parameter_value(parameter1, parameter1_mode)
            parameter2_value = self.get_parameter_value(parameter2, parameter2_mode)
            if parameter1_value != 0:
                self.pointer = parameter2_value
            else:
                self.pointer += 3
        elif current_opcode == 6:
            parameter1, parameter2 = self.intcode[self.pointer+1:self.pointer+3]
            parameter1_value = self.get_parameter_value(parameter1, parameter1_mode)
            parameter2_value = self.get_parameter_value(parameter2, parameter2_mode)
            if parameter1_value == 0:
                self.pointer = parameter2_value
            else:
                self.pointer += 3
        elif current_opcode in [1, 2, 7, 8]:
            # get three parameters for addition/multiplication
            parameter1, parameter2, parameter3 = self.intcode[self.pointer+1:self.pointer+4]
            parameter1_value = self.get_parameter_value(parameter1, parameter1_mode)
            parameter2_value = self.get_parameter_value(parameter2, parameter2_mode)

            if current_opcode == 1:
                self.intcode[parameter3] = parameter1_value + parameter2_value
            elif current_opcode == 2:
                self.intcode[parameter3] = parameter1_value * parameter2_value
            elif current_opcode == 7:
                self.intcode[parameter3] = 1 if parameter1_value < parameter2_value else 0
            elif current_opcode == 8:
                self.intcode[parameter3] = 1 if parameter1_value == parameter2_value else 0
            self.pointer += 4