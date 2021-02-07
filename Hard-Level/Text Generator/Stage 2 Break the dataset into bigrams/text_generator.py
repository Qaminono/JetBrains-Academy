PATH = input()
tokens = list()
with open(PATH, "r", encoding="utf-8") as file:
    for line in file:
        tokens.extend(line.split())

unique_tokens = set(tokens)
bigrams = list(zip(tokens[:-1], tokens[1:]))

print(f"Number of bigrams: {len(bigrams)}")

is_work = True
while is_work:
    choice = input()
    if choice == "exit":
        is_work = False
        break
    try:
        choice = int(choice)
        if choice < 0:
            print("Head: the       Tail: North!")
        else:
            print(f"Head: {bigrams[choice][0]}\t\tTail: {bigrams[choice][1]}")
    except (TypeError, ValueError):
        print("Type Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please input a value that is not greater than the number of all bigrams.")
