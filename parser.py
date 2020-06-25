import json

# get the article texts from mls_pubs.json
text = []

# opens the file and iterates through each line, adding the text to the dict
with open('data/microwave_limb_sounder/mls_pubs.json') as f:
    for line in f:
            j = json.loads(line)
            text.append(json.loads(line).get("_source").get("text"))

# check that data has all the lines. Keeping for future reference
# print(len(text))
# shocker, it does

# save first line to a .txt file
# line = open('line.txt','w+')
# may need to add code to save texts to a .txt, so keeping