import json
import spacy
from sys import argv

script, json_file = argv

# Get the article texts from mls_pubs.json
titles = []
articles = []

# Opens the file and iterates through each line
# Adds titles and article texts to dicts
source = open(json_file)
for line in source:
        j = json.loads(line)
        titles.append(j.get("_source").get("title"))
        articles.append(j.get("_source").get("text"))
            
# Save it all to a text file
# file = open('articles.json','w+')
# for i in text:
#     file.(i)

# file.close()
# Commenting out, may not need to save to a file of any sort
# May need to add code to save texts to a .txt, so keeping

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = articles[0]
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

# Adapted from spaCy website