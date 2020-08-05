import json
import spacy
import random

training_data = []

train_file = open("spacy_annotations.jsonl")

for line in train_file:
    j = json.loads(line)
    training_data.append(j)

nlp = spacy.load("en_core_web_sm")

for itn in range(100):
    random.shuffle(training_data)
    losses = (training_data, size=compounding(4.0,32.0,1.001))
    for batch in batches