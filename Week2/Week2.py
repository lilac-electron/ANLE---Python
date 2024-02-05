import nltk
from nltk.corpus import wordnet as wn, wordnet_ic as wn_ic, lin_thesaurus as lin
import scipy
from scipy import stats
from gensim.models import KeyedVectors

import ssl
import csv

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

#nltk.download('wordnet')


#print(wn.synsets('book',wn.NOUN)[1].definition())
for book in wn.synsets('book', wn.NOUN):
    #print(book.definition())
    pass
var = wn.synsets('book',wn.NOUN)[1]
#print(var.hyponyms()[0].definition())
#print(var.hypernyms())

def Path_Similarity(noun1, noun2):
    max = 0.0
    for noun1_noun in noun1:
        for noun2_noun in noun2:
            similarity = noun1_noun.path_similarity(noun2_noun)
            if similarity > max:
                max = similarity
    return max
    
def generalSimilarityScore(noun1, noun2, option=''):
    noun_set1 = wn.synsets(noun1, wn.NOUN)
    noun_set2 = wn.synsets(noun2, wn.NOUN)
    max = 0.0
    brown_ic=wn_ic.ic("ic-brown.dat")
    if option == 'res':
        for noun1_it in noun_set1:
            for noun2_it in noun_set2:
                similarity = noun1_it.res_similarity(noun2_it, brown_ic)
                if similarity > max:
                    max = similarity 
    if option == 'lin':
        for noun1_it in noun_set1:
            for noun2_it in noun_set2:
                similarity = noun1_it.lin_similarity(noun2_it, brown_ic)
                if similarity > max:
                    max = similarity 
    if option == '':
        for noun1_it in noun_set1:
            for noun2_it in noun_set2:
                similarity = noun1_it.path_similarity(noun2_it)
                if similarity > max:
                    max = similarity 
    return max
#print(wn.synsets('chicken', wn.NOUN)[0].path_similarity(wn.synsets('car', wn.NOUN)[0]))

#print(Path_Similarity(wn.synsets('chicken', wn.NOUN), wn.synsets('car', wn.NOUN)))
#print(generalSimilarityScore('chicken', 'car', 'res'))
#print(generalSimilarityScore('chicken', 'car', 'lin'))
#print(generalSimilarityScore('chicken', 'car', ''))

mcdata_dict = dict()
with open('Week2/wk2labresources/mcdata.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if len(row) == 3:
            key = tuple(row[:2])
            val = [float(row[2])]
            mcdata_dict[key] = val
#print(mcdata_dict)
for key in mcdata_dict.keys():
    mcdata_dict[key].append([generalSimilarityScore(key[0], key[1], 'res')])
    mcdata_dict[key][1].append(generalSimilarityScore(key[0], key[1], 'lin'))
    #mcdata_dict[key][1].append(generalSimilarityScore(key[0], key[1]))
    #generalSimilarityScore(key[0], key[1], 'res')

resList = []
linList =[]
huObv =[]
for value in mcdata_dict.values():
    resList.append(value[1][0])
    linList.append(value[1][1])
    huObv.append(value[0])
#print (resList)
#print(linList)
#print(huObv)
def judgePVal(p):
    if p < 0.05:
        print("Reject hypothesis as p less than 0.05")
#cor, p = scipy.stats.spearmanr(resList, linList)
#judgePVal(p)
print(scipy.stats.spearmanr(resList, huObv))
print(scipy.stats.spearmanr(linList, huObv))

filename = 'Week2/wk2labresources/GoogleNews-vectors-negative300.bin'
mymodel = KeyedVectors.load_word2vec_format(filename, binary=True)
print(mymodel.similarity('man', 'woman'))
googleDict = dict()
googleSimList = []
for key in mcdata_dict.keys():
    googleDict[key] = mymodel.similarity(key[0], key[1])
    googleSimList.append(mymodel.similarity(key[0], key[1]))
#print(googleDict)
print(scipy.stats.spearmanr(googleSimList, huObv))
print(scipy.stats.spearmanr(googleSimList, resList))
print(scipy.stats.spearmanr(googleSimList, linList))
#print(mcdata_dict)
    