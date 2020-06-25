import json

# get the JSON from mls_pubs.json
# data = []
text = []

with open('data/microwave_limb_sounder/mls_pubs.json') as f:
    for line in f:
            j = json.loads(line)
            text.append(json.loads(line).get("_source").get("text"))
            # print(j.get("_source").get("text"))
            # break

# text = data[0].get("_source").get("text")
print(text[500])

# check that data has all the lines
print(len(text))
# shocker, it does

# print first line
# change this code because you realize that Python has 0 indexing
# print(data[0])


# save first line to a .txt file
# line = open('line.txt','x+')
# deprecated, need to dump to a json file. Should have added this comment earlier

# with open('line.json','w+') as line:
#     json.dump(data[2],line)

# print(data[0]['text'])