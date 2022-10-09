from nltk import pos_tag
from nltk import word_tokenize
import nltk

sample_text = "Trump economic advisor Larry Kudlow told Fox Business Wednesday that the administration supports " \
              "measures to increase oversight of Chinese firms, though the White House hasn't publicly stated an " \
              "opinion on this particular legislation."

tokenized_words = word_tokenize(sample_text)
tag = pos_tag(tokenized_words)

namedEnt = nltk.ne_chunk(tag, binary=True)
namedEnt.draw()
