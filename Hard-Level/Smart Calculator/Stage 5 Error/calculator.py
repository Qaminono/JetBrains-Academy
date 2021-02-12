while True:
    a = b = 0
    input_line = input()
    if input_line.startswith("/"):
        commands = {"/help": "The program calculates the sum of numbers",
                    "/exit": "Bye!"}
        print(commands.get(input_line, "Unknown command"))
        if input_line == "/exit":
            break
    elif input_line:
        try:
            print(eval(input_line, {"__builtins__": None}))
        except:
            print("Invalid expression")
    else:
        pass
