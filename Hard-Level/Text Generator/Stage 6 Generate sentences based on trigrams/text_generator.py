from collections import defaultdict, Counter
from string import ascii_uppercase
import random

PATH = input()
tokens = list()
with open(PATH, "r", encoding="utf-8") as file:
    for line in file:
        tokens.extend(line.split())

unique_tokens = set(tokens)
trigrams = list(zip(tokens[:-2], tokens[1:-1], tokens[2:]))


def trigram_checker(sequence_lst):
    for i in range(len(sequence_lst) - 2):
        trigram = tuple(sequence_lst[i: i + 3])
        if trigram in trigrams:
            pass
        else:
            return False
    return True


trigrams_freqs = Counter([" ".join((trigram[0], trigram[1],  trigram[2])) for trigram in trigrams])
trigrams_dict = defaultdict(list)

for trigram in trigrams_freqs:
    *head, tail = trigram.split()
    trigrams_dict[' '.join(head)].append((tail, trigrams_freqs[trigram]))

for value in trigrams_dict.values():
    value.sort(key=lambda x: x[1], reverse=True)

counter = 0
while counter < 10:
    sequence = list()
    list_of_start_words = tuple(filter(lambda x: x[0] in ascii_uppercase and x[-1] not in ".?!", trigrams_dict.keys()))
    bigram = random.choice(list_of_start_words)
    sequence.extend(bigram.split())
    if sequence[0][-1] in ".?!":
        continue
    pop_counter = 0
    while True:
        list_of_words = [value[0] for value in trigrams_dict[bigram]]
        list_of_weights = [value[1] for value in trigrams_dict[bigram]]
        next_word = random.choices(population=list_of_words, weights=list_of_weights)[0]
        sequence.append(next_word)
        bigram = bigram.split()[1] + " " + next_word
        if len(sequence) < 5 and sequence[-1][-1] in ".?!":
            sequence.pop()
            pop_counter += 1
            if pop_counter > 10:
                break
        if len(sequence) >= 5 and sequence[-1][-1] in ".?!":
            break

    if not trigram_checker(sequence):
        continue
    print(" ".join(sequence))
    counter += 1
