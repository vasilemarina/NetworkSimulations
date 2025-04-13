import random

def read_valid_message():
    while True:
        message = input("Introduceti mesajul: ")
        if len(message) % 7 != 0:
            print("Lungimea mesajului trebuie sa fie multiplu de 7.")
        elif not all(bit in "01" for bit in message):
            print("Mesajul trebuie sa contina doar 0 si 1.")
        else:
            return message

def create_parity_matrix(message):
    rows = len(message) // 7
    matrix = [[int(message[row*7+col]) for col in range(7)] for row in range(rows)]

    for row in matrix:
        row.append(sum(row) % 2)

    columns_parity = [(sum(matrix[row][col] for row in range(rows))) % 2 for col in range(7)]
    matrix.append(columns_parity + [sum(columns_parity) % 2])

    return matrix

def corrupt_message(message):
    corrupted_index = random.randint(0, len(message)-1)
    corrupted_message = list(message)
    corrupted_message[corrupted_index] = '0' if message[corrupted_index] == '1' else '1'

    return ''.join(corrupted_message)

def get_corrupted_bit(parity_matrix):
    error_row, error_col = None, None

    for row in range(len(parity_matrix) - 1):
        if sum(int(parity_matrix[row][col]) for col in range(len(parity_matrix[row])-1)) % 2 != parity_matrix[row][-1]:
            error_row = row
            break

    for col in range(len(parity_matrix[0])-1):
        if sum(int(parity_matrix[row][col]) for row in range(len(parity_matrix)-1)) % 2 != parity_matrix[-1][col]:
            error_col = col
            break

    return error_row * 7 + error_col

def get_corrupted_parity_matrix(matrix, corrupted_message):
    corrupted_matrix = matrix.copy()

    found = False
    index = 0
    for row in range(len(corrupted_matrix)-1):
        for col in range(len(corrupted_matrix[0])-1):
            if corrupted_matrix[row][col] != int(corrupted_message[index]):
                corrupted_matrix[row][col] = int(corrupted_message[index])
                found = True
                break
            index += 1
        if found:
            break

    return corrupted_matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
    print()

def main():
    message = read_valid_message()
    parity_matrix = create_parity_matrix(message)

    print()
    print('Matricea de paritate:')
    print_matrix(parity_matrix)

    corrupted_message = corrupt_message(message)
    print('Mesajul corupt: ' + corrupted_message + '\n')

    corrupted_matrix = get_corrupted_parity_matrix(parity_matrix, corrupted_message)

    print('Mesajul transmis prin retea: ')
    print(''.join(''.join(''.join(map(str, row))) for row in corrupted_matrix) + '\n')

    print('Pozitia bitului corupt:', end=' ')
    print(get_corrupted_bit(corrupted_matrix) + 1)

if __name__ == "__main__":
    main()