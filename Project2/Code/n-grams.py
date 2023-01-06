import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import re
import pandas as pd

dataPath = '~/SocialMediaMining/Project2/Data/mergedMensRightsRed.csv'
df = pd.read_csv(dataPath, engine='python')

#unigrams
words = df.comment_body

#bigrams
bigrams = (pd.Series(nltk.ngrams(words, 3)).value_counts())

#trigrams
trigrams = (pd.Series(nltk.ngrams(words, 3)).value_counts())

#4-grams
frGrams = (pd.Series(nltk.ngrams(words, 4)).value_counts())

#new column in df
df['unigrams'] = words
df['bigrams'] = bigrams
df['trigrams'] = trigrams
df['4-grams'] = frGrams

#Export
print('exporting POS tagged file')
df.to_csv('~/SocialMediaMining/Project2/Data/mergedMensRightsGrams.csv', index=False)
