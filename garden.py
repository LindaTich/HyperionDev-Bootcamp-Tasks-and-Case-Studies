'''Start
Create a file named garden.py, save in VS Code.
Import spaCy and added two sentences to list gardenpathSentences.
Add three further sentences as given in the task.
Tokenize using .orth and named entity recognition using .ents.
Use spacy.explain to look up and name entities.
Comment on two of the entities and answer the questions.
End'''

import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["The prime number few", "When Fred eats food gets thrown", "Mary gave the child a Band-Aid", "That Jill is never here hurts", "The cotton clothing is made of grows in Mississippi"] 

doc = nlp(gardenpathSentences)

[token.orth_ for token in doc]

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

nlp_gardenpath = nlp(gardenpathSentences)
print([(i, i.label_, i.label) for i in nlp_gardenpath.ents])

print(spacy.explain("FAC"))

entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")

# "FAC" refers to something factual.

# If an event has taken place then this will be factual.

# If someone has done or said something, this will be a fact.

print(spacy.explain("PERSON"))

entity_person = spacy.explain("PERSON")
print(f"PERSON:{entity_person}")

# "PERSON" refers to a name or a noun.

# Person refers to a mentioned person through name.

# If someone is named, first or last name then this entity is used.