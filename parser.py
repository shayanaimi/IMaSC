import json

# get the JSON from mls_pubs.json
data = []
with open('data/microwave_limb_sounder/mls_pubs.json') as f:
    for line in f:
            data.append(json.loads(line))

# print first line
# change this code because you realize that Python has 0 indexing
print(data[0])

# save first line to a .txt file
#line = open('line.txt','x+')

with open('line.txt','x+') as line:
    line.write('' + data[0])