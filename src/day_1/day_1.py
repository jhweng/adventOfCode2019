

def main():
    # Read input from file
    try:
        with open('day_1_input.txt') as f:
            str_lst_input = f.readlines()

        int_lst_input = [int(str_input.strip('\n')) for str_input in str_lst_input]

        req_fuel_lst = []
        for mass in int_lst_input:
            req_fuel = int(mass/3 - 2)
            extra_fuel = req_fuel

            while extra_fuel > 0:
                extra_fuel = int(extra_fuel/3 - 2)

                if extra_fuel > 0:
                    req_fuel += extra_fuel

            req_fuel_lst.append(req_fuel)

        total_req_fuel = 0
        for fuel in req_fuel_lst:
            total_req_fuel += fuel

        print(total_req_fuel)

    except IOError:
        print('Could not read input as \'day_1_input.txt\'')


if __name__ == '__main__':
    main()

