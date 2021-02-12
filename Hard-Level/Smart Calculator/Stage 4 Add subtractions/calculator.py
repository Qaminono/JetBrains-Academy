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
        print(eval(input_line, {"__builtins__": None, "input_line": input_line}))
    else:
        pass
