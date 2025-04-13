from random import randint

class Computer:
    computers_num = 0

    @staticmethod
    def generate_ip_address(computers):
        bytes = []
        unique = False
        while not unique:
            unique = True
            bytes = []
            for i in range(4):
                bytes.append(str(randint(0, 255)))

            for computer in computers:
                if '.'.join(bytes) == computer.ip_address:
                    unique = False
                    break

        return '.'.join(bytes)

    def print_state(self):
        print('C' + str(self.id) + '(' + self.ip_address + ')-> ' + self.buffer)

    def __init__(self):
        self.id = self.computers_num
        Computer.computers_num += 1

        self.ip_address = ''
        self.buffer = 'null'