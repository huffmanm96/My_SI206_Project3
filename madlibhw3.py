# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# making a new commit 5
from nltk.book import *
from nltk import bigrams
import nltk
import random
from nltk import word_tokenize,sent_tokenize

print("START*******")
print("\n\n")

tokens = text2[:150]


tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples


tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "ADV":"an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1,"ADV":.1}

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

print("\n\n")

old_text = " ".join(tokens)
new_text = "".join(final_words)

print ("Original text:" + str(old_text))
print("\n\n")
print ("New text:" + new_text)


# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text


print("\n\nEND*******")
