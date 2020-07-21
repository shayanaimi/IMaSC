import json
import random
import os
import codecs
import numpy as np
import re
from re import search

# jsonl_source = path to a file that we will read from
# jsonl_output = path to the file that we will write to
def get_article_text(
    jsonl_source="data/microwave_limb_sounder/mls_pubs.jsonl",
    jsonl_output="data/microwave_limb_sounder/article_text.jsonl",
):
    # Dict for each article, may need more than the title and text
    articles = {}
    #articles["title"] = []
    articles["text"] = []
    text = ""

    # Opens the source and output and iterates through each line of the source
    # Adds titles and article texts to dict
    source = open(jsonl_source)
    output = open(jsonl_output, "w+")

    # Regular expression pattern to find unicode escapes and hex escapes
    # unicode_remove = re.compile(r"\\[uU]([a-zA-Z0-9_]{4})")
    # hex_remove = re.compile(r"\\[xX]([a-zA-Z0-9_]{2})")

    for line in source:
        j = json.loads(line)
        #articles["title"] = j.get("_source").get("title")
        text = j.get("_source").get("text")

        # Splits text at the paragraph level (as best as it can be done)
        chunks = text.split('\n\n')

        # Adds dict, in JSON form, to output, line by line
        for i in chunks:

            if len(i) < 100:
                continue

            # Remove all unicode and hex escapes
            text = remove_escapes(i)

            # Clean the strings of other escapes and dump to temporary output file
            cleaned_string = clean_text(text)
            articles["text"] = cleaned_string
            json.dump(articles, output)
            output.write("\n")

    output.close()

# article_text is the original parsed article text file
# The sets are my training, validation, and testing sets for Prodigy
def shuffle_article_text(
    article_text="data/microwave_limb_sounder/article_text.jsonl",
    training_set="data/microwave_limb_sounder/training_set.jsonl",
    validation_set="data/microwave_limb_sounder/validation_set.jsonl",
    testing_set="data/microwave_limb_sounder/testing_set.jsonl",
    random_seed = 1742
):

    np.random.seed(random_seed)

    # Open the original file and assigns a random number to each line
    with open(article_text,'r') as source:
        data = [(np.random.rand(), line) for line in source]
        source.close()
    
    # Sorts the data by the random number
    data.sort()

    # Writes 70% of shuffled text to training set and 15% each to validation
    # and testing sets (70 + 15 + 15 = 100)
    training = open(training_set, "w+")
    validation = open(validation_set, "w+")
    testing = open(testing_set, "w+")

    for j in range(len(data)):

        if j < len(data)*0.7:
            training.write(data[j][1])
        elif j >= len(data)*0.7 and j < len(data)*0.85:
            validation.write(data[j][1])
        else:
            testing.write(data[j][1])  
        
    training.close()
    validation.close()
    testing.close()
    os.remove(article_text)


def sortByLength(o):
    return len(o)

def remove_escapes(text):
    # Remove unicode escapes
    unicode_remove = re.compile(r"\\[uU]([a-zA-Z0-9_]{4})")
    text = re.sub(unicode_remove, "", text.encode('unicode_escape').decode())

    # Remove hex escapes
    hex_remove = re.compile(r"\\[xX]([a-zA-Z0-9_]{2})")
    text = re.sub(hex_remove, "", text)

    # Removes \n and other escapes
    text = re.sub(r"\\[a-zA-Z]", " ", text) # whatever \\n is
    text = re.sub(r"\\R", " ", text) # Should cover all line breaks
    text = re.sub(r"\"", "", text) # Exact match for whatever \" is

    return text

def clean_text(text):
        # simple text cleaning to remove some unicode representations
        text = text.replace("-\n", "")  # word broken over line break
        text = text.replace("\u00a0", "")  # empty space
        text = text.replace("\u2022", "; ")  # bullet
        text = text.replace("\u201c", "'")  # left double quotation mark
        text = text.replace("\u201d", "'")  # right double quotation mark
        text = text.replace("\u03b7", "GREEK_ETA")  # greek eta
        text = text.replace("\u03b1", "GREEK_ALPHA")  # greek alpha
        text = text.replace("\u03b3", "GREEK_GAMMA")  # greek eta
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
        text = text.replace("\u0000", "")  # null character
        text = text.replace("\u00b0", " degrees")  # degrees
        text = text.replace("\\\\", "") # get rid of random backslashes
        text = text.replace("\\\"", "") # get rid of random quotes

        return text

# Executes the script
if __name__ == "__main__":
    get_article_text()
    shuffle_article_text()
