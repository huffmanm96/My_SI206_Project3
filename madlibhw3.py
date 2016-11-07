# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

#Starting mad lib for a commit
from nltk.book import *
from nltk import bigrams
import nltk
import random
from nltk import word_tokenize,sent_tokenize

print(text1)
print(text2)

print("\n\n")

tokens = nltk.word_tokenize(text2)
print("TOKENS")
print(tokens)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
print("TAGGED TOKENS")
print(tagged_tokens)
if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:5]:
		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}
substitution_probabilities = {"NN":.1,"NNS":.2,"VB":.25,"JJ":.25}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))


# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")


print("\n\nEND*******")
