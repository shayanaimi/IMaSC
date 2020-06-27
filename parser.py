import json
from sys import argv

# Expects 3 arguments: script name, the jsonl source file (mls_pubs.jsonl), and
# the jsonl output file name (must be a .jsonl for annotation)
script, jsonl_source, jsonl_output = argv

# Dict for each article, may need more than the title and text
articles = {}
articles["title"] = []
articles["text"] = []


# Opens the source and output and iterates through each line of the source
# Adds titles and article texts to dict
# Adds dict, in JSON form, to output, line by line
source = open(jsonl_source)
output = open(jsonl_output, "w+")

for line in source:
    j = json.loads(line)
    articles["title"] = j.get("_source").get("title")
    articles["text"] = j.get("_source").get("text")
    json.dump(articles, output)
    output.write('\n')

output.close()