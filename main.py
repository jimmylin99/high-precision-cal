from addition import addition
from subtraction import subtraction
from division import division
from multiplication import multiplication
from utils import exit_program, remove_prefix_zero


def command_line_interface():
    def is_valid(x):
        _float_cnt = 0
        for i, c in enumerate(x):
            if i == 0 and c == '-':
                continue
            if c in map(str, range(0, 10)):
                continue
            if c == '.':
                if _float_cnt == 0:
                    _float_cnt += 1
                    continue
            return False
        return True

    # forever-loop
    while True:
        _choice = 0
        while _choice not in [1, 2, 3, 4]:
            _choice = \
                input('Please select calculation type\n' +
                      'Type 1 for addition, 2 for subtraction, \n' +
                      '3 for multiplication, 4 for division\n' +
                      'To exit the program, just type `exit` or `quit`\n'
                      'Your choice: ')
            if _choice in ['exit', 'quit']:
                exit_program()

            try:
                _choice = int(_choice)
            except ValueError:
                print('-' * 20 + '\n' +
                      'A ValueError occurred. Please Type the calculation type with correct form.\n' +
                      '-' * 20)

        # simulation of the switch-case clause
        switch = {
            1: lambda: print('-' * 20 + '\n' + 'Addition: a + b'),
            2: lambda: print('-' * 20 + '\n' + 'Subtraction: a - b'),
            3: lambda: print('-' * 20 + '\n' + 'Multiplication: a * b'),
            4: lambda: print('-' * 20 + '\n' + 'Division: a / b')
        }
        switch[_choice]()

        precision = None
        while True:
            a = input('a = ')
            b = input('b = ')
            if is_valid(a) and is_valid(b):
                break
            else:
                print('Invalid input of `a` or(and) `b`')
            if _choice == 4:  # division
                precision = input('precision [default 10] = ')
                if precision == '':
                    precision = 10
                    break
                try:
                    precision = int(precision)
                except ValueError:
                    print('Invalid input of `precision`')
                    continue
                if precision < 0:
                    print('Invalid range of `precision`, non-negative value is required')
                    continue

        switch = {
            1: addition,
            2: subtraction,
            3: multiplication,
            4: division
        }
        _args = [a, b, precision] if precision else [a, b]
        err_code, result = switch[_choice](*_args)  # execute corresponding high precision calculation
        if err_code != 'OK':
            print(err_code)
        else:
            print('-' * 10 + 'Result' + '-' * 10)
            result = remove_prefix_zero(result)  # for human readability
            switch = {
                1: lambda: print(f'a + b = {a} + {b} = {result}'),
                2: lambda: print(f'a - b = {a} - {b} = {result}'),
                3: lambda: print(f'a * b = {a} * {b} = {result}'),
                4: lambda: print(f'a / b = {a} / {b} = {result}')
            }
            switch[_choice]()
            print('-' * 26)

        # end of each calculation, request for another round
        _continue = 0
        while _continue not in ['Y', 'y', 'N', 'n', '']:  # if simply press ENTER, then continue
            _continue = input('Do you want to try again? [Y/n]: ')
        if _continue in ['Y', 'y', '']:
            continue
        if _continue in ['N', 'n']:
            exit_program()


if __name__ == '__main__':
    command_line_interface()
