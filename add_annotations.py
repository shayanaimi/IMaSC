import json

spans = []
item = {}
item["start"] = 0
item["end"] = 0
item["token_start"] = 0
item["token_end"] = 0
item["label"] = ""

instruments = ["MLS", "Microwave Limb Sounder", "SMR", "Sub-Millimetre Radiometer", 
"ACE-FTS", "Fourier Transform Ultra-Violet Spectrometer", "SCIAMACHY"]
spacecraft = []
models = []
experiments = ["ACE","Atmospheric Chemistry Experiment"]
locations = []

#Take in data from annotations - Copy.jsonl
#for each JSON
# Check if we have spans
# if yes, spans = spans, if no initialize spans
#text = JSON text
# Substring checking

spans.append(item)
spans.append(item)


print(spans)
