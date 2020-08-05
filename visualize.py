import spacy
from spacy import displacy

colors = {"SPACECRAFT": "#b35f50", "INSTRUMENT":"#509cb3"}
print(type(colors))
options = {"ents": ["SPACECRAFT","INSTRUMENT"], "colors": colors}

text = "We will show with scatter diagrams of water vapor and ozone mixing ratios from the balloon soundings that there are signicant seasonal differences in the contributions from wave, source, and path variability. We augment the analysis by comparing the variance in the balloon soundings to simulated proles constructed from water vapor and ozone data from the Aura Microwave Limb Sounder (MLS) using a new reverse domain lling technique."

nlp = spacy.load("models")
doc = nlp(text)
displacy.serve(doc, style="ent", options=options)