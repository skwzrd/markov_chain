import re
import os
from collections import defaultdict
from random import randint, choice

SENTENCE_LENGTH = 9

FILE = './ramblings.txt'
FILE = os.path.abspath(FILE)

# {word: {next_word1: count1, next_word2: count2, ...}}
word_dict = defaultdict(dict)


def scrub_line(line):
    line = line.replace('\'', '')
    line = re.sub(r'[^a-zA-Z]', ' ', line)
    line = re.sub(r'\s{2,}', ' ', line)
    line = line.lower()
    return line


def make_word_dict():
    """Open up a text file containing any sort of coherent text.
        Any non letters are removed from the text."""
    with open(FILE, 'r') as f:
        for line in f.readlines():
            line = scrub_line(line)
            if line=='':
                continue
            sentence_words = line.split(' ')
            sentence_words.remove('')
            # It could be a good idea to keep track of which words
            # are most frequently found at the end of sentences
            # and terminate sentences there, rather than using SENTENCE_LENGTH
            for i, word in enumerate(sentence_words[:-1]):
                next_word = sentence_words[i+1]
                try:
                    word_dict[word][next_word] += 1
                except:
                    word_dict[word][next_word] = 1


def get_next_word(current_word):
    """Given a word, find another word that is likely to come after it.
        We do this based on our word_dict."""
    next_words = word_dict[current_word]
    word_sum = sum(next_words.values())

    rndm = randint(1, word_sum)
    for (word, count) in next_words.items():
        rndm -= count
        if rndm <= 0:
            return word
    raise ValueError('Didn\'t find a next word.')


def build_sentence():
    """Choose a word to begin the sentence with.
        Add additional words up to a set number, SENTENCE_LENGTH."""
    sentence = ''
    word_dict_keys = list(word_dict.keys())
    start_word = choice(word_dict_keys)
    current_word = start_word
    sentence+=start_word.title()+' '

    for _i in range(0, SENTENCE_LENGTH):
        current_word = get_next_word(current_word)
        sentence+=current_word+' '

        # if word has no next word (i.e. if its not in word_dict.keys())
        # end the sentence.
        if current_word not in word_dict_keys:
            break

    sentence=sentence[:-1]+'.'
    return sentence


if __name__ == "__main__":
    make_word_dict()
    sentence = build_sentence()
    print(sentence)
