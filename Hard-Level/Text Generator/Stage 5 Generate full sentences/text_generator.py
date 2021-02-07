from collections import defaultdict, Counter
from string import ascii_uppercase
import random

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

counter = 0
while counter < 10:
    sequence = list()
    list_of_start_words = tuple(filter(lambda x: x[0] in ascii_uppercase and x[-1] not in ".?!", bigrams_dict.keys()))
    sequence.append(random.choice(list_of_start_words))
    pop_counter = 0
    while True:
        list_of_words = [value[0] for value in bigrams_dict[sequence[len(sequence) - 1]]]
        list_of_weights = [value[1] for value in bigrams_dict[sequence[len(sequence) - 1]]]
        sequence.extend(random.choices(population=list_of_words, weights=list_of_weights))
        if len(sequence) < 5 and sequence[-1][-1] in ".?!":
            sequence.pop()
            pop_counter += 1
            if pop_counter > 10:
                break
        if len(sequence) >= 5 and sequence[-1][-1] in ".?!":
            print(" ".join(sequence))
            counter += 1
            break
