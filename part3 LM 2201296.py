
import nltk
import json
from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict

model = defaultdict(lambda: defaultdict(lambda: 0))

for sentence in reuters.sents():
    for char1, char2, char3 in trigrams(sentence, pad_right=True, pad_left=True):
        model[(char1, char2)][char3] += 1
 
for char1_char2 in model:
    total_count = float(sum(model[char1_char2].values()))
    for char3 in model[char1_char2]:
        model[char1_char2][char3] /= total_count


print(json.dumps(dict(model['he','is']),indent=3,sort_keys=3))

print('\n')

import random

text = ["he", "is"]

def printText():
    sentence_finished = False
    while not sentence_finished:

        r = random.random()
        accumulator = .0

        for word in model[tuple(text[-2:])].keys():
            accumulator += model[tuple(text[-2:])][word]
            if accumulator >= r:
                text.append(word)
                break

        if text[-2:] == [None, None]:
            sentence_finished = True
        
    return(' '.join([t for t in text if t]))


print(printText())
