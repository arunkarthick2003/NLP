from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# sample_sentence = "Stopwords are a pretty cool way of getting rid of the words that we do not want"
stop_words = set(stopwords.words("english"))
print(stop_words)
#
# tokenized_words = word_tokenize(sample_sentence)
#
# filtered_sentence = []
#
# for word in tokenized_words:
#     if word not in stop_words:
#         filtered_sentence.append(word)
#
# print(filtered_sentence)

with open("2001aspaceodyssey.txt", "r") as corpora:
    sample_text = corpora.read()

tokenized_sentences = sent_tokenize(sample_text)
for sentence in tokenized_sentences:
    tokenized_words = word_tokenize(sentence)

    filtered_sentence = []

    for word in tokenized_words:
        word = word.lower()  # skip this first time
        if word not in stop_words:
            filtered_sentence.append(word)

    print(filtered_sentence)
