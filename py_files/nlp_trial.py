fhand = open("/Users/jamey_hansen/Documents/Pycharm_projects/IS_452/Final_Project/git_452_final/data_gathering/DPS_Stage4", "r")
filein = fhand.read()  # my text string
fhand.close()

lines = filein.split("/n")  # my text as list of lines
for line in lines:
    print(line)

import re # remove punctuation
import nltk  #use nltk for tokenization, stemming, lemmatizing
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
stopwords = set(stopwords.words("english"))
import spacy
# || from part_of_speech import get_part_of_speech  # get method to identify pos
nlp = spacy.load("en") # load spacy -- English
doc = nlp(filein) # pass in text to spacy nlp object, filein string is the text-15 syllabi



cleaned = re.sub('\W+', ' ', filein) # substitute space in place of one or more non alphanumberic character (clean punctuation)
tokenized = word_tokenize(cleaned) # split cleaned strings based on spaces into tokenized objects - words
no_stop_tokenized = [word for word in tokenized if not word in stopwords] # list of words excluding stopwords
print("token objects without stop words: ")
print(no_stop_tokenized)

print()
print()
tagged = nltk.pos_tag(no_stop_tokenized)# tag list of words excluding stopwords by part of speech
print("TYPE:")
print(type(tagged))  # check to see why tagged didn't work, it's a list!
print("tagged token objects:")
print(tagged)

for entity in doc.ents:
    print(entity.text, entity.label_)
