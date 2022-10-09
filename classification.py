import nltk
from nltk.corpus import movie_reviews
import random

# (['this', 'movie', 'is', 'great'], 'pos')

documents = []
for category in movie_reviews.categories():
    # print(category)
    for fileid in movie_reviews.fileids(category):
        # print(fileid)
        ##########
        review_word_list = list(movie_reviews.words(fileid))
        # print(review_word_list)
        # break
        ########
        document = (review_word_list, category)
        documents.append(document)

# print(documents[0])
random.shuffle(documents)
# print(documents[0])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
# print(all_words.most_common(10))
# print(len(all_words))
# print(all_words["brilliant"])

############################################

word_features = []
for common_word in all_words.most_common(3000):
    word_features.append(common_word[0])


def find_features(feature_doc):
    words = set(feature_doc)
    features = {}
    # {'name': 'Bob'}
    for word in word_features:
        is_feature_in_words = word in words
        features[word] = is_feature_in_words

    return features


# print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

featuresets = []
for (review, category) in documents:
    feature = (find_features(review), category)
    featuresets.append(feature)

############################################

training_set = featuresets[:1500]
test_set = featuresets[1500:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Accuracy : ", nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(15)
