import spacy
nlp = spacy.load('en_core_web_md')

# Example word similarity
tokens = nlp("cat apple monkey banana")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# apple and banana are similar as both are fruit
# monkey and cat are similar as both are animals
# monkey and banana are similar, as monkey's eat bananas

# Own Word similarity example
tokens = nlp("chocolate movies popcorn television books")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# I thought there would be higher similarities between books, movies and television than there are


print("\n")


# Example sentence similarity
model_sentence = nlp("Why is my cat on the car")

sentences = ["Where did my dog go?",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Sentence 3 is the most similar as it recognizes that there is a car



# Example Code Comments
# Produces this error using en_core_web_sm instead of en_core_web_md
# Produces similarity based on the words used, not the sentence
# Similarities tend to be lower because of this
"""
The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the 
tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the 
small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. 
You can always add your own word vectors, or use one of the larger models instead if available.
print(token.similarity(token_))
"""

