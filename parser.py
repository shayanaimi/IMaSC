import json
from sys import argv

# Expects 3 arguments: script name, the jsonl source file (mls_pubs.jsonl), and
# the jsonl output file name (must be a .jsonl for annotation)
# script, source, output = argv
# Currently removing command line arguments


def get_article_text(
    jsonl_source="data/microwave_limb_sounder/mls_pubs.jsonl",
    jsonl_output="data/microwave_limb_sounder/article_text.jsonl",
):
    # Dict for each article, may need more than the title and text
    articles = {}
    articles["title"] = []
    articles["text"] = []
    text = ""
    sentences = []

    # Opens the source and output and iterates through each line of the source
    # Adds titles and article texts to dict
    # Adds dict, in JSON form, to output, line by lines
    source = open(jsonl_source)
    output = open(jsonl_output, "w+")

    for line in source:
        j = json.loads(line)
        articles["title"] = j.get("_source").get("title")
        # articles["text"] = j.get("_source").get("text")
        text = j.get("_source").get("text")
        sentences = text.split('\n')
        for i in sentences:
            articles["text"] = i
            json.dump(articles, output)
            output.write("\n")

    output.close()


# Executes the script
if __name__ == "__main__":
    get_article_text()
