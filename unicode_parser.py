import json
import random
import os
import codecs
import re
from re import search

# jsonl_source = path to a file that we will read from
# jsonl_output = path to the file that we will write to
def get_unicode_text(
    jsonl_source="data/microwave_limb_sounder/mls_pubs.jsonl",
    jsonl_output="data/microwave_limb_sounder/unicode_text.jsonl",
):
    # Dict for each article, may need more than the title and text
    articles = {}
    articles["text"] = []
    text = ""
    sentences = []

    # Opens the source and output and iterates through each line of the source
    # Adds titles and article texts to dict
    source = open(jsonl_source)
    output = open(jsonl_output, "w+")

    for line in source:
        j = json.loads(line)
        text = j.get("_source").get("text")

        # Splits text at the sentence level (as best as it can be done)
        chunks = text.split('\n\n')
        chunks.sort(key=sortByLength)

        # Adds dict, in JSON form, to output, line by line
        for i in chunks:

            # print(type(i))

            if len(i) < 50:
                continue
            
            cleaned_string = clean_text(i)
            raw_string = r"{cleaned_string}"

            substring = r"\"

            if search(substring, raw_string):
                print("Found!")
                articles["text"] = i
                json.dump(articles, output)
                output.write("\n")
                

    output.close()

def to_raw(string):
    return r"{string}"

def sortByLength(o):
    return len(o)

def clean_text(text):

        # simple text cleaning to remove some unicode representations
        text = text.replace("\u00a0", "")  # empty space
        text = text.replace("\u2022", "; ")  # bullet
        text = text.replace("\u201c", "'")  # left double quotation mark
        text = text.replace("\u201d", "'")  # right double quotation mark
        text = text.replace("-\n", "")  # word broken over line break
        text = text.replace("\n", " ")  # line break
        text = text.replace("\u03b7", "GREEK_ETA")  # greek eta
        text = text.replace("\u03b1", "GREEK_ALPHA")  # greek alpha
        text = text.replace("\u03b3", "GREEK_GAMMA")  # greek eta
        text = text.replace("\t", " ")  # tab
        text = text.replace("\u2212", "-")  # minus sign
        text = text.replace("\u002B", "+")  # plus sign
        text = text.replace("\u2206", "INCREMENT")  # increment
        text = text.replace("\u2264", "<=")  # less than equal to
        text = text.replace("\u2265", ">=")  # greater than equal to
        text = text.replace("\u2013", "-")  # dash
        text = text.replace("\u03b5", "GREEK_EPSILON")  # greek small letter epsilon
        text = text.replace("\u03a6", "GREEK_PHI")  # greek phi
        text = text.replace("\u2026", "...")  # horizontal elipsis
        text = text.replace("\u2018", "'")  # right single quote
        text = text.replace("\u2019", "'")  # left single quote
        text = text.replace("\u03c4", "GREEK_TAU")  # greek tau
        text = text.replace("\u00b5", "MICRO_SIGN")  # greek tau
        text = text.replace("\u00b5", "GREEK_LAMBDA")  # greek lambda
        text = text.replace("\u03c3", "GREEK_SIGMA")  # greek sigma
        text = text.replace("\u20ac", "EURO")  # greek sigma
        text = text.replace("\u2215", "/")  # division slash
        text = text.replace("\u00e4", "ae")  # a umlaut
        text = text.replace("\u00e8", "e")  # small latin e
        text = text.replace("\u25e6", "")  # bullet
        text = text.replace("\u00b1", "+-")  # plus minus sign
        text = text.replace("\u2032", "PRIME")  # prime
        text = text.replace("\ud835", " ")  # invalid character
        text = text.replace("\udf0e", " ")  # invalid character
        text = text.replace("\u00a9", "COPYRIGHT")  # copyright
        text = text.replace("\u2191", "UP_ARROW")  # arrow
        text = text.replace("\u2192", "RIGHT_ARROW")  # arrow
        text = text.replace("\u2190", "LEFT_ARROW")  # arrow
        text = text.replace("\u2193", "DOWN_ARROW")  # arrow
        text = text.replace("\u2194", "LEFT_RIGHT_ARROW")  # arrow
        text = text.replace("\u00a0", "_")  # no break space
        text = text.replace("\f", "")  # page break
        text = text.replace("\u0000", "")  # null character
        text = text.replace("\u00b0", " degrees")  # degrees
        text = re.sub("[\(\[].*?[\)\]]", "", text) # remove parentheses and brackets and what's inside them
        
        return text

# Executes the script
if __name__ == "__main__":
    get_unicode_text()