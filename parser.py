import json
from sys import argv

# jsonl_source = path to a file that we will read from
# jsonl_output = path to the file that we will write to
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
    source = open(jsonl_source)
    output = open(jsonl_output, "w+")

    for line in source:
        j = json.loads(line)
        articles["title"] = j.get("_source").get("title")
        text = j.get("_source").get("text")

        # Splits text at the sentence level (as best as it can be done)
        sentences = text.split('.')

        # Adds dict, in JSON form, to output, line by line
        for i in sentences:
            articles["text"] = i
            json.dump(articles, output)
            output.write("\n")

    output.close()

# Executes the script
if __name__ == "__main__":
    get_article_text()
