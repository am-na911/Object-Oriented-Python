def input_is_valid(user_input, start=0, end=None):
    while True:
        inp = input(user_input)

        if not inp.isdecimal():
            print('Input is invalid!')

        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('invalid range. Try again!')
            else:
                return int(inp)
            
        else:
            return int(inp)


