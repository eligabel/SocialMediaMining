import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.util import ngrams
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import re
import pandas as pd

dataPath = '~/SocialMediaMining/Project2/Data/mergedAskRed.csv'
df = pd.read_csv(dataPath, engine='python')

words = df['comment_body']
#unigrams
listdf = words.tolist()

wordlist = []

for i in listdf:
	unigram = nltk.word_tokenize(str(i))
	wordlist.append(unigram)

#bigrams
bigramlist = []

for i in wordlist:
	bigram = list(ngrams(i, 2))
	bigramlist.append(bigram)

#trigrams
trigramlist = []

for i in wordlist:
	trigram = list(ngrams(i, 3))
	trigramlist.append(trigram)

#4-grams
frgramlist = []

for i in wordlist:
	frgram = list(ngrams(i, 4))
	frgramlist.append(frgram)

#new column in df
df['unigrams'] = wordlist
df['bigrams'] = bigramlist
df['trigrams'] = trigramlist
df['4-grams'] = frgramlist


#Export
print('exporting ngram file')
df.to_csv('~/SocialMediaMining/Project2/Data/mergedAskRedGrams.csv', index=False)
