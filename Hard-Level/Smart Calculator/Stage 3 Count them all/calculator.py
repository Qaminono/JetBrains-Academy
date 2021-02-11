while True:
    a = b = 0
    input_line = input()
    if input_line.startswith("/"):
        commands = {"/help": "The program calculates the sum of numbers",
                   "/exit": "Bye!"}
        print(commands[input_line])
        if input_line == "/exit":
            break
    elif input_line:
        print(sum(map(int, input_line.split())))
    else:
        pass
