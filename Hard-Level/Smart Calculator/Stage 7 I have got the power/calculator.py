from string import digits, ascii_uppercase, ascii_lowercase


def input_check_line(line):
    line.replace(' ', '')
    left, *right = line.split("=")
    if line.count("=") > 1:
        print("Invalid assignment")
        return False
    if set(left) & set(digits):
        print("Invalid identifier")
        return False
    if set(right) & set(ascii_lowercase) & set(ascii_uppercase) and right not in globals():
        print("Invalid assignment")
        return False
    return True


while True:
    input_line = input().strip()
    if input_line.startswith("/"):
        commands = {"/help": "The program calculates the sum of numbers",
                    "/exit": "Bye!"}
        print(commands.get(input_line, "Unknown command"))
        if input_line == "/exit":
            break
    elif input_line:
        try:
            if '**' in input_line or "//" in input_line:
                raise Exception
            if "=" in input_line:
                if input_check_line(input_line):
                    exec(input_line)
            else:
                print(int(eval(input_line)))
        except NameError:
            print("Unknown variable")
        except:
            print("Invalid expression")
    else:
        pass
