def read_valid_input():
    while True:
        message = input("Introduceti mesajul: ")
        generator = input("Introduceti polinomul generator(cu coeficienti 0 si 1): ")

        if not all(bit in "01" for bit in message) or not all(bit in "01" for bit in generator):
            print("Sirurile trebuie sa contina doar 0 si 1.")
        elif len(message) <= len(generator):
            print("Lungimea mesajului trebuie sa fie mai mare decat a polinomului generator.")
        else:
            return message, generator.lstrip('0')

def get_poly_degree(coefficients):
    front_zeros = 0
    for bit in coefficients:
        if bit == '1':
            break
        front_zeros += 1

    return len(coefficients) - 1 - front_zeros

def extend_poly(coefficients, zeros_num):
    extended_poly = list(coefficients)
    while zeros_num:
        extended_poly.append('0')
        zeros_num -= 1

    return ''.join(extended_poly)

def xor(x, y):
    if len(x) < len(y):
        x, y = y, x

    result = ['0' if x[i] == y[i] else '1' for i in range(len(y))]
    for i in range(len(y), len(x)):
        result.append(x[i])

    return ''.join(result)

def binary_sum(x, y):
    if len(x) < len(y):
        x, y = y, x

    result = [x[i] for i in range(len(x) - len(y))]
    result += [str(int(x[len(x) - len(y) + i]) + int(y[i])) for i in range(len(y))]
    return ''.join(result)

def polynomial_division(x, y):
    rest = xor(x, y)
    while len(x) >= len(y):
        rest = xor(x, y)
        x = rest.lstrip('0')
        print(x)

    return x

def main():
    message, generator_coefficients = read_valid_input()

    extend_poly_coefficients = extend_poly(message, get_poly_degree(generator_coefficients))
    print('\nPolinomul extins: ', extend_poly_coefficients)

    print('\nResturile impartirilor: ')
    rest = polynomial_division(extend_poly_coefficients, generator_coefficients)
    print('\nRest:', rest)

    print('\nMesajul transmis: ')
    print(binary_sum(extend_poly_coefficients, rest))

if __name__ == "__main__":
    main()