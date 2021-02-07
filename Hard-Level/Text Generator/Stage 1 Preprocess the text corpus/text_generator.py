PATH = input()
tokens = list()
with open(PATH, "r", encoding="utf-8") as file:
    for line in file:
        tokens.extend(line.split())

unique_tokens = set(tokens)

print(f"""Corpus statistics
All tokens: {len(tokens)}
Unique tokens: {len(unique_tokens)}""")

is_work = True
while is_work:
    choice = input()
    if choice == "exit":
        is_work = False
        break
    try:
        choice = int(choice)
        if choice < 0:
            print("North!")
        else:
            print(tokens[choice])
    except (TypeError, ValueError):
        print("Type Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")
