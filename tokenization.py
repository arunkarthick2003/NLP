# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:47:52 2022

@author:Arunkarthick
"""
from nltk.tokenize import sent_tokenize, word_tokenize
text="Hello there Mr. Abishek, how are you? The weather is nice today. How is your mother-in-law doing?"
#sent_tokenize is sentence tokenizer
tokenized_sentence=sent_tokenize(text)
for sentence in tokenized_sentence:
    print(sentence)
    
tokenized_word=word_tokenize(text)
for word in tokenized_word:
    print(word)