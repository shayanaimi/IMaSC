import json

# Get the JSON from mls_pubs.json
data = []
with open('data/microwave_limb_sounder/mls_pubs.json') as f:
    for line in f:
            data.append(json.loads(line))

# Print first line
print(data[1])