from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps=PorterStemmer()
# =============================================================================
# sample_words=["illegal","legal","leganize","legally"]
# for word in sample_words:
#     print(ps.stem(word))
# =============================================================================
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
# =============================================================================
# print(lemmatizer.lemmatize("puppies"))
# =============================================================================
print(lemmatizer.lemmatize("better",pos="a"))