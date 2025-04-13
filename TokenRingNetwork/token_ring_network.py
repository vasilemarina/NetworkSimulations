from computer import Computer
from network_token import NetworkToken
import random

class TokenRingNetwork:
    directions = {'trighonometric': 1, 'clockwise': 2}

    def print_computers_state(self):
        for computer in self.computers:
            computer.print_state()

    def generate_source_and_destination(self):
        source = random.randint(0, self.computers_number - 1)
        while True:
            destination = random.randint(0, self.computers_number - 1)
            if source != destination:
                break

        return source, destination

    def next_computer(self, current_computer_index):
        if TokenRingNetwork.directions['trighonometric'] == self.direction:
            return current_computer_index - 1 \
                if current_computer_index - 1 >= 0 else Computer.computers_num - 1
        else:
            return current_computer_index + 1 \
                if current_computer_index + 1 < Computer.computers_num else 0

    def print_simulation_step(self):
        source_index, destination_index = self.generate_source_and_destination()
        print('Sursa: C' + str(self.computers[source_index].id) +
              ' Destinatia: C' + str(self.computers[destination_index].id))

        if self.current_computer_index is None:
            self.current_computer_index = source_index
            print('C' + str(self.computers[source_index].id) + ': Muta jetonul')
        else:
            while self.current_computer_index != source_index:
                self.token.history += ' C' + str(self.computers[self.current_computer_index].id)
                print('C' + str(self.computers[self.current_computer_index].id) + ': Muta jetonul')
                self.current_computer_index = self.next_computer(self.current_computer_index)

            print('C' + str(self.computers[source_index].id) + ': Am preluat jetonul')
            print('C' + str(self.computers[source_index].id) + ': Muta jetonul')

        self.token.load_token(' C' + str(self.computers[source_index].id), self.computers[destination_index].id,
                              self.messages.readline().rstrip('\n'))
        self.current_computer_index = self.next_computer(self.current_computer_index)

        while True:
            self.token.history += ' C' + str(self.computers[self.current_computer_index].id)
            if self.computers[self.current_computer_index].ip_address == self.computers[destination_index].ip_address:
                print('C' + str(self.computers[self.current_computer_index].id) + ': Am ajuns la destinatie')
                self.computers[self.current_computer_index].buffer += ';' + self.token.message
                self.token.reached_destination = True
                print('C' + str(self.computers[self.current_computer_index].id) + ': Muta jetonul')
            elif self.computers[self.current_computer_index].ip_address == self.computers[source_index].ip_address:
                print('C' + str(self.computers[self.current_computer_index].id) + ': Am ajuns inapoi')
                self.token.reached_destination = False
                self.token.free = True
                break
            else:
                print('C' + str(self.computers[self.current_computer_index].id) + ': Muta jetonul')

            self.current_computer_index = self.next_computer(self.current_computer_index)

        for computer in self.computers:
            computer.print_state()
        print('Istoricul token-ului: ' + self.token.history)
        self.token.history = ''

    def print_simulation(self, simulation_steps):
        for i in range(simulation_steps):
            self.print_simulation_step()
            print()

    def __init__(self, computers_number, direction, messages):
        self.computers_number = computers_number
        self.computers = [Computer() for _ in range(computers_number)]
        self.token = NetworkToken()
        self.direction = direction
        self.messages = messages
        self.current_computer_index = None

        for computer in self.computers:
            computer.ip_address = computer.generate_ip_address(self.computers)