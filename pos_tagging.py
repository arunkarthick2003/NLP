from nltk import pos_tag
from nltk import word_tokenize, sent_tokenize

''' POS Tag list:

    CC coordinating conjunction
    CD cardinal digit
    DT determiner
    EX existential there (like: "there is" ... think of it like "there exists")
    FW foreign word
    IN preposition/subordinating conjunction
    JJ adjective 'big'
    JJR adjective, comparative 'bigger'
    JJS adjective, superlative 'biggest'
    LS list marker 1)
    MD modal could, will
    NN noun, singular 'desk'
    NNS noun plural 'desks'
    NNP proper noun, singular 'Harrison'
    NNPS proper noun, plural 'Americans'
    PDT predeterminer 'all the kids'
    POS possessive ending parent's
    PRP personal pronoun I, he, she
    PRP$ possessive pronoun my, his, hers
    RB adverb very, silently,
    RBR adverb, comparative better
    RBS adverb, superlative best
    RP particle give up
    TO to go 'to' the store.
    UH interjection errrrrrrrm
    VB verb, base form take
    VBD verb, past tense took
    VBG verb, gerund/present participle taking
    VBN verb, past participle taken
    VBP verb, sing. present, non-3d take
    VBZ verb, 3rd person sing. present takes
    WDT wh-determiner which
    WP wh-pronoun who, what
    WP$ possessive wh-pronoun whose
    WRB wh-abverb where, when
'''

# sample_text = "I was walking by the road when I saw the cutest puppy on the other side"
#
# tokenized_words = word_tokenize(sample_text)
# tag = pos_tag(tokenized_words)
# print(tag)

with open("2001aspaceodyssey.txt", "r") as corpora:
    sample_text = corpora.read()

# print(sample_text)

tokenized_sentences = sent_tokenize(sample_text)
for sentence in tokenized_sentences:
    tokenized_words = word_tokenize(sentence)
    tag = pos_tag(tokenized_words)
    print(tag)

