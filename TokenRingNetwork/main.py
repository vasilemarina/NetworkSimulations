import fileinput

from token_ring_network import TokenRingNetwork

def get_direction(directions):
    while True:
        print('Alegeti sensul jetonului prin retea:')
        print('1- sens trigonometric')
        print('2- sens invers')

        choise = input()
        if choise == '1':
            return directions['trighonometric']
        elif choise == '2':
            return directions['clockwise']
        else:
            print('Alegere invalida.')

def main():
    computers_num = 10
    simulation_steps = 10

    direction = get_direction(TokenRingNetwork.directions)
    filename = 'messages.txt'
    messages = fileinput.input(filename)
    network = TokenRingNetwork(computers_num, direction, messages)

    network.print_computers_state()
    print()
    network.print_simulation(simulation_steps)

if __name__ == '__main__':
    main()