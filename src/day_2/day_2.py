def main():
    try:
        with open('day_2_input.txt') as f:
            str_lst_input = f.readlines()

            size = 4
            for input_line in str_lst_input:
                single_program_line = [int(elem.strip()) for elem in input_line.split(',')]

                # split_program_lines = [single_program_line[i:i+size] for i in range(0,len(single_program_line), size)]
                print(single_program_line)
                # print(split_program_lines)
                for i in range(0, len(single_program_line), size):
                    if single_program_line[i] == 1:  # add
                        single_program_line[i+3] = single_program_line[i+1] + single_program_line[i+2]
                        print('soma')
                    elif single_program_line[i] == 2:  # multiply
                        single_program_line[i + 3] = single_program_line[i + 1] * single_program_line[i + 2]
                        print('multiplica')
                    elif single_program_line[i] == 99:  # halt
                        print('break')
                        break
                    else:
                        print('Error during decoding program!')

                print(single_program_line)
                print(single_program_line[0])


    except IOError:
        print('Could not read input as \'day_2_input_txt\'')


if __name__ == '__main__':
    main()