from collections import defaultdict, Counter
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

for _ in range(10):
    sequence = list()
    sequence.append(random.choice(tuple(bigrams_dict.keys())))
    for i in range(9):
        list_of_words = [value[0] for value in bigrams_dict[sequence[i]]]
        list_of_weights = [value[1] for value in bigrams_dict[sequence[i]]]
        sequence.extend(random.choices(population=list_of_words, weights=list_of_weights))
    print(" ".join(sequence))
