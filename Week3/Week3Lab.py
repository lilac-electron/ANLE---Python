import nltk
from nltk.corpus import wordnet as wn, wordnet_ic as wn_ic, lin_thesaurus as lin
import scipy
from scipy import stats
from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
import numpy as np
import json

import ssl
import csv

filename = 'Week2/wk2labresources/GoogleNews-vectors-negative300.bin'
mymodel = KeyedVectors.load_word2vec_format(filename, binary=True)
#print(mymodel['man'])
with open('Week3/relations.json', 'r') as fp:
    testtuples=json.load(fp)
#print(testtuples['capital-common-countries'])
capital_countries = testtuples['capital-common-countries']
#print(mymodel.most_similar(positive=['China','London'],negative=['England']))

def predict(country,training_pair):
    #similarity = mymodel.similarity('Athens', 'Greece')
    similarity = mymodel.similarity(training_pair[0], training_pair[1])
    list_of_similarities = mymodel.most_similar(positive=[country, training_pair[0]], negative=[training_pair[1]])
    #most_similar = 0
    #most_similar_capital = ''
    #for each in list_of_similarities:
    #    if each[1] >= similarity and each[1] > most_similar:
    #        most_similar = each[1]
    #        most_similar_capital = each[0]
    #if most_similar_capital == '':
    most_similar_capital = list_of_similarities[0][0]
    #print("Prediction for,"+ country+", is:"+most_similar_capital)
    return most_similar_capital

print(len(capital_countries))
def task2():
    correct = 0
    #incorrect = 0
    total = 0
    for training_pair in capital_countries:
        for pair in capital_countries:
            if pair[0] == training_pair[0]:
                pass
            else:
                #The second element in the pair is the country
                total += 1
                prediction = predict(pair[1], training_pair)
                if prediction == pair[0]:
                    correct += 1
                #else:
                #    incorrect += 1
    print((correct/total)*100)
task2()