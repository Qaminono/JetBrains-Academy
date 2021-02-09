while True:
    a = b = 0
    input_line = input()
    if input_line == "/exit":
        print("Bye!")
        break
    elif input_line:
        print(sum(map(int, input_line.split())))
    else:
        pass
