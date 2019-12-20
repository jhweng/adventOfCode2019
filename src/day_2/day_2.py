def main():
    try:
        with open('day_2_input.txt') as f:
            str_lst_input = f.readlines()

            size = 4
            for input_line in str_lst_input:
                lst_program = [int(elem.strip()) for elem in input_line.split(',')]

                # print(lst_program)
                lst_program[1] = 12
                lst_program[2] = 2

                for i in range(0, len(lst_program), size):
                    opcode = lst_program[i]

                    if opcode == 99:
                        break

                    operand_1_index = lst_program[i+1]
                    operand_2_index = lst_program[i+2]
                    dst_index = lst_program[i+3]
                    
                    if opcode == 1:  # add
                        lst_program[dst_index] = lst_program[operand_1_index] + lst_program[operand_2_index]
                        # print('soma')
                    elif opcode == 2:  # multiply
                        lst_program[dst_index] = lst_program[operand_1_index] * lst_program[operand_2_index]
                        # print('multiplica')
                    else:
                        print('Error during decoding program!')

                # print(lst_program)
                print(lst_program[0])

    except IOError:
        print('Could not read input as \'day_2_input_txt\'')


if __name__ == '__main__':
    main()

