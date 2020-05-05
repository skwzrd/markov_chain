# Image Board

#### Set Up
Add a text file called `ramblings.txt` to the same directory as `markov.py`. Have this file contain a reasonable number of sentences.

#### Basic Principles
A dictionary is going to be generated from the sentences in `ramblings.txt` with the structure `{word_A: {succeeding_word_A1: count_A1, succeeding_word_A2: count_A2, ...}, word_B:{...}...}`. An example of this dictionary is:
```python

ramblings = "The dog chased the dog around the yard."
# forms the dicitonary:
word_dict = {
    'the': {
        'dog': 2,
        'yard': 1,
    },
    'dog': {
        'chased': 1,
        'around': 1
    },
    'chased': {
        'the': 1
    },
    'around': {
        'the': 1
    }
}
```
With this dicitonary, when we're given a word, we can calculate a probability of another word succeeding it, and then use that probabilistic word to build a string of words (a sentence).

Sentences begin by choosing a random word from `word_dict`'s keys, and they end if (1) the set sentence length is reached, or (2) if a word has no successors.

#### Examples
```python
>>> py markov.py
"Someone insists on the importance of southeast china and studies."

>>> py markov.py
"Only real programming language for the best language for days."

>>> py markov.py
"Snapshot of the place was earning really my main chat."
```

Obviously these sentences not very coherent, but they're fun to read nonetheless.
