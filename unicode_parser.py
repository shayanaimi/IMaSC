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

            if len(i) < 5000:
                continue

            text = re.sub(r"\\u([\da-f]{4})", "", i)

            # if getStringWithDecodedUnicode(i):
            # print("Found!")
            articles["text"] = text
            json_str = json.dumps(articles)
            output.write(json_str)
            output.write("\n")
        
    output.close()

def sortByLength(o):
    return len(o)

# # Taken from StackOverflow
# def getStringWithDecodedUnicode( value ):
#     findUnicodeRE = 
#     # def getParsedUnicode(x):
#     #     return chr( int( x.group(1), 16 ) )

def clean_text(text):

        # simple text cleaning to remove some unicode representations
        text = text.replace("-\n", "")  # word broken over line break
        text = text.replace("\n", " ")  # line break
        text = text.replace("\u2013", "-")
        text = text.replace("\ufb01", "fi")
        text = text.replace("\ufb02", "fl")
        text = text.replace("\u00b0", " degrees ")
        text = text.replace("\u000E", "")
        text = text.replace("\u0006", "")
        text = text.replace("\u0002", "")
        text = text.replace("\u0018", "")
        text = text.replace("\u2019", "'")
        text = text.replace("\u2018", "'")
        text = text.replace("\u00b4", "")
        text = text.replace("\u00bc", "1/4")
        text = text.replace("\u00a8", "")
        text = text.replace("\u00b1", "+-")
        text = text.replace("\u00ad", "-")
        text = text.replace("\u00bb", ">>")
        text = text.replace("\u2014", "-")
        text = text.replace("\u00a7", "")
        text = text.replace("\u0019", "")
        text = text.replace("\u0001", "")
        text = text.replace("\u0014", "")
        text = text.replace("\u00de", "")
        text = text.replace("\u00f0", "")
        text = text.replace("\u0010", "")
        text = text.replace("\u00bd", "1/2")
        text = text.replace("\u00fe", "")
        text = text.replace("\u0003", "")
        text = text.replace("\u001d", "")
        text = text.replace("\u001c", "")
        text = text.replace("\u008a", "S")
        text = text.replace("\u00f8", "o")
        text = text.replace("\u2010", "-")
        text = text.replace("\u25e6", "")
        text = text.replace("\u25cf", "")
        text = text.replace("\u2212", "-")
        text = text.replace("\u00e1", "")
        text = text.replace("\u201c", "\"")
        text = text.replace("\u201d", "\"")
        text = text.replace("\u00d7", "x")
        text = text.replace("\u00f6", "o")
        text = text.replace("\u00ef", "i")
        text = text.replace("\u00fc", "u")
        text = text.replace("\u00e4", "a")
        text = text.replace("\ud835", "")
        text = text.replace("\udc74", "")
        text = text.replace("\udc7f", "")
        text = text.replace("\u03c8", "Greek psi")
        text = text.replace("\u00ed", "i")
        text = text.replace("\u00a0", "")  # empty space
        text = text.replace("\u2022", "; ")  # bullet
        text = text.replace("\u201c", "'")  # left double quotation mark
        text = text.replace("\u201d", "'")  # right double quotation mark
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
        # text = re.sub("[\(\[].*?[\)\]]", "", text) # remove parentheses and brackets and what's inside them
        
        return text

# Executes the script
if __name__ == "__main__":
    get_unicode_text()