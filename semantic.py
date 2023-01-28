# T38

""" NOTES FOR REVIEWER """

""" Similarities between cat, monkey and banana and my own examples:
Where words are identical, they return a value of 1.0
The language model can recognize groups (eg. animals, fruits) and returns
higher correlations for items in the same group.
The higher the correlation, the closer linked they are.
The order of the comparison (eg. cat vs monkey, monkey vs cat) doesn't make any 
difference. 
The model seems to have some idea of how alike different animals are, eg. 
monkey / ape returns 0.99, cow / horse returns 0.54, horse / pony returns 0.65.
"""

""" Running example files with complex / simple models gives different 
results.  The simple model is less good at identifying similarities and also
doesn't rate the sentence similarities in the same order - if you were using
this to pick a 'winner', you'd get different results.

I calculated and reviewed these statistics : 

Complaints vs complaints: 

Average correlation     0.860	    0.613
Median correlation      0.869	    0.572
Standard deviation      0.050005646 0.102916316

Recipes vs recipes:

Average correlation     0.893	    0.708
Median correlation      0.897	    0.718
Standard deviation      0.030253267	0.057393074

Recipes vs complaints:

Average	correlation     0.675	    0.444
Median	correlation     0.697	    0.490
Standard deviation 	    0.100420952	0.170755338


"""

import spacy

option = input("a for advanced, else will default to simple model : ")

if option.lower() == "a":
    # Advanced language model
    nlp = spacy.load('en_core_web_md')
else:
    # Simple language model
    nlp = spacy.load('en_core_web_sm')



# SIMILARITY WITH SPACY ========================================================

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# WORKING WITH VECTORS =========================================================

tokens = nlp('cat monkey ape')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))  

# WORKING WITH SENTENCES =======================================================

sentence_to_compare = "Why is my cat on the car"
sentences = ["Where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
