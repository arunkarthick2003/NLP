# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 13:22:11 2023

@author: hp
"""

import nltk
import gensim
from gensim.models import Word2Vec
from nltk.corpus import stopwords
import re

paragraph="""Avul Pakir Jainulabdeen Abdul Kalam (/ˈɑːbdəl kəˈlɑːm/ (listen); 15 October 1931 – 27 July 2015) was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007. He was born and raised in Rameswaram, Tamil Nadu and studied physics and aerospace engineering. He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian space programme and military missile development efforts.[1] He thus came to be known as the Missile Man of India for his work on the development of ballistic missile and launch vehicle technology.[2][3][4] He also played a pivotal organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974.
Kalam was elected as the 11th president of India in 2002 with the support of both the ruling Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the "People's President",[6] he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several prestigious awards, including the Bharat Ratna, India's highest civilian honour."""

#processing the data
text=re.sub(r'\[[0-9]"\]',' ',paragraph)
text=re.sub(r'\s+',' ',text)
text=text.lower()
text=re.sub(r'\d',' ',text)
text=re.sub(r'\s+',' ',text)

#preparing the dataset
sentences=nltk.sent_tokenize(text)
sentences=[nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i]=[word for word in sentences[i] if word not in stopwords.words('english')]
    
#training the word2vec model
model=Word2Vec(sentences,min_count=1)

model.wv.index_to_key

#finding word vectors
vector=model.wv['kalam']

#most similar words
similar=model.wv.most_similar('kalam')

