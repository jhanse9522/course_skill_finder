import re
import numpy as np

my_sentences=["I am hello", "I am cat!", "I am flying."]


def word_extraction(sentence):  # takes one sentence and cleans it one at a time
    ignore = ['a', "the", "is"]  # stop words
    words = re.sub("[^\w]", " ",  sentence).split()  #substitute space for any non word character in sentence and split on space
    cleaned_text = [w.lower() for w in words if w not in ignore]  # do , for loop, within list comp, save it in var, return it
                                                                    # gives each result of for loop
    return cleaned_text


def tokenize(allsentences):  # takes all sentences
    words = []
    for sentence in allsentences:
        w = word_extraction(sentence)    # call function above and save, text cleaned
        words.extend(w)         # build list of the cleaned text using accumulator
        words = sorted(list(set(words)))
        # get a list of the unique set of words and sort and save
        print(words)
        return words


def generate_bow(allsentences):  # starts the engine

    vocab = tokenize(allsentences)   # call above function, which calls function above that

    print("Word List for Document \n{0} \n".format(vocab))


    for sentence in allsentences:
    words = word_extraction(sentence)
    bag_vector = [len(vocab) * str(0)]
    bag_vector = int(bag_vector)   # should be bag_vector = numpy.zeros(len(vocab))
    for w in words: # loop over cleaned text sentence
    for i,word in enumerate(vocab): # loop over vocab set, enumerated
    if word == w:  # compare the two, if same value
    bag_vector[i] += 1 #increment zero value vector by 1 for that word
    print("{0}\n{1}\n".format(sentence,numpy.array(bag_vector)))

my_bag = generate_bow(my_sentences)
