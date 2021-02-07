from collections import defaultdict, Counter

PATH = input()
tokens = list()
with open(PATH, "r", encoding="utf-8") as file:
    for line in file:
        tokens.extend(line.split())

unique_tokens = set(tokens)
bigrams = list(zip(tokens[:-1], tokens[1:]))

bigrams_freqs = Counter([" ".join(bigram) for bigram in bigrams])
bigrams_dict = defaultdict(list)

for bigram in bigrams_freqs:
    head, tail = bigram.split()
    bigrams_dict[head].append((tail, bigrams_freqs[bigram]))

for value in bigrams_dict.values():
    value.sort(key=lambda x: x[1], reverse=True)

is_work = True
while is_work:
    choice = input()
    if choice == "exit":
        is_work = False
        break
    print(f"Head: {choice}")
    if bigrams_dict[choice]:
        for tail in bigrams_dict[choice]:
            print(f"Tail: {tail[0]}    Count: {tail[1]}")
    else:
        print("The requested word is not in the model. Please input another word.")
