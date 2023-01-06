import re
import math
import numpy as np
from itertools import chain
from collections import Counter
import nltk
from nltk.util import ngrams
import pandas as pd

dataPath1 = '~/SocialMediaMining/Project2/Data/mergedAskRedGrams.csv'
df1 = pd.read_csv(dataPath1, engine='python')

dataPath2 = '~/SocialMediaMining/Project2/Data/mergedFemGrams.csv'
df2 = pd.read_csv(dataPath2, engine='python')

dataPath3 = '~/SocialMediaMining/Project2/Data/mergedMensRightsGrams.csv'
df3 = pd.read_csv(dataPath3, engine='python')

#define lists of each ngram from each dataframe

ask1 = df1['unigrams']
ask2 = df1['bigrams']
ask3 = df1['trigrams']
ask4 = df1['4-grams']

fem1 = df2['unigrams']
fem2 = df2['bigrams']
fem3 = df2['trigrams']
fem4 = df2['4-grams']

men1 = df3['unigrams']
men2 = df3['bigrams']
men3 = df3['trigrams']
men4 = df3['4-grams']

#write to lists
listask1 = ask1.tolist()
listask2 = ask2.tolist()
listask3 = ask3.tolist()
listask4 = ask4.tolist()

listfem1 = fem1.tolist()
listfem2 = fem2.tolist()
listfem3 = fem3.tolist()
listfem4 = fem4.tolist()

listmen1 = men1.tolist()
listmen2 = men2.tolist()
listmen3 = men3.tolist()
listmen4 = men4.tolist()

def jaccard_distance(a, b):
#Calculate the jaccard distance between sets A and B
	a = set(a)
	b = set(b)
	return 1.0 * len(a&b)/len(a|b)

def cosine_similarity_ngrams(a, b):
	vec1 = Counter(a)
	vec2 = Counter(b)

	intersection = set(vec1.keys()) & set(vec2.keys())
	numerator = sum([vec1[x] * vec2[x] for x in intersection])

	sum1 = sum([vec1[x]**2 for x in vec1.keys()])
	sum2 = sum([vec2[x]**2 for x in vec2.keys()])
	denominator = math.sqrt(sum1) * math.sqrt(sum2)

	if not denominator:
		return 0.0
	return float(numerator) / denominator

#define variables for test
a1 = listask1
b1 = listmen1
a2 = listask2
b2 = listmen2
a3 = listask3
b3 = listmen3
a4 = listask4
b4 = listmen4

AM1 = "Jaccard: {}   Cosine: {}".format(jaccard_distance(a1,b1), cosine_similarity_ngrams(a1,b1))
AM2 = "Jaccard: {}   Cosine: {}".format(jaccard_distance(a2,b2), cosine_similarity_ngrams(a2,b2))
AM3 = "Jaccard: {}   Cosine: {}".format(jaccard_distance(a3,b3), cosine_similarity_ngrams(a3,b3))
AM4 = "Jaccard: {}   Cosine: {}".format(jaccard_distance(a4,b4), cosine_similarity_ngrams(a4,b4))

AMres1 = ("Ask1xMen1:" + AM1)
AMres2 = ("Ask2xMen2:" + AM2)
AMres3 = ("Ask3xMen3:" + AM3)
AMres4 = ("Ask4xMen4:" + AM4)

AMresFull = (AMres1 + AMres2 + AMres3 + AMres4)

c1 = listask1
d1 = listfem1
c2 = listask2
d2 = listfem2
c3 = listask3
d3 = listfem3
c4 = listask4
d4 = listfem4

AFres1 = ("Ask1xFem1:" + "Jaccard: {}   Cosine: {}".format(jaccard_distance(c1,d1), cosine_similarity_ngrams(c1,d1)))
AFres2 = ("Ask2xFem2:" + "Jaccard: {}   Cosine: {}".format(jaccard_distance(c2,d2), cosine_similarity_ngrams(c2,d2)))
AFres3 = ("Ask3xFem3:" + "Jaccard: {}   Cosine: {}".format(jaccard_distance(c3,d3), cosine_similarity_ngrams(c3,d3)))
AFres4 = ("Asf4xFem4:" + "Jaccard: {}   Cosine: {}".format(jaccard_distance(c4,d4), cosine_similarity_ngrams(c4,d4)))

AFresFull = (AFres1 + AFres2 + AFres3 + AFres4)

e1 = listfem1
f1 = listmen1
e2 = listfem2
f2 = listmen2
e3 = listfem3
f3 = listmen3
e4 = listfem4
f4 = listmen4

FMres1 = ("Fem1xMen1:" + "Jaccard: {}   Cosine: {}".format(jaccard_distance(e1,f1), cosine_similarity_ngrams(e1,f1)))
FMres2 = ("Fem2xMen2:" + "Jaccard: {}   Cosine: {}".format(jaccard_distance(e2,f2), cosine_similarity_ngrams(e2,f2)))
FMres3 = ("Fem3xMen3:" + "Jaccard: {}   Cosine: {}".format(jaccard_distance(e3,f3), cosine_similarity_ngrams(e3,f3)))
FMres4 = ("Fem4xMen4:" + "Jaccard: {}   Cosine: {}".format(jaccard_distance(e4,f4), cosine_similarity_ngrams(e4,f4)))

FMresFull = (FMres1 + FMres2 + FMres3 + FMres4)

print('writing reports')

report = open('resultsAskxMen.txt', 'w')
report.write(AMresFull)

report = open('resultsAskxFem.txt', 'w')
report.write(AFresFull)

report = open('resultsFemxMen.txt', 'w')
report.write(FMresFull)
