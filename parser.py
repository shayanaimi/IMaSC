import json
import random
import os
import codecs

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
    sentences = []

    # Opens the source and output and iterates through each line of the source
    # Adds titles and article texts to dict
    source = open(jsonl_source)
    output = open(jsonl_output, "w+")

    for line in source:
        j = json.loads(line)
        #articles["title"] = j.get("_source").get("title")
        text = j.get("_source").get("text")

        # Splits text at the sentence level (as best as it can be done)
        chunks = text.split('\n\n')
        chunks.sort(key=sortByLength)

        # Adds dict, in JSON form, to output, line by line
        for i in chunks:
            # print(i)
            cleaned_string = clean_text(i)
            articles["text"] = cleaned_string
            json.dump(articles, output)
            output.write("\n")
        
        break

    output.close()

# article_text is the original parsed article text file
# The sets are my training, validation, and testing sets for Prodigy
def shuffle_article_text(
    article_text="data/microwave_limb_sounder/article_text.jsonl",
    training_set="data/microwave_limb_sounder/training_set.jsonl",
    validation_set="data/microwave_limb_sounder/validation_set.jsonl",
    testing_set="data/microwave_limb_sounder/testing_set.jsonl"
):

    # Open the original file and randomize the order
    with open(article_text,'r') as source:
        data = [(random.random(), line) for line in source]
        source.close()
    
    # Sorts the data (not entirely sure why this works, but hey)
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

def clean_text(text, scrub_nums=False, scrub_names=False):
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
        text = text.replace("\u0000", "_")  # no break space
        text = text.replace("cost", "")  # word cost
        text = text.replace(";", "")  # word cost
        # text = re.sub("[\(\[].*?[\)\]]", "", text) # remove parentheses and brackets and what's inside them

        if scrub_nums:
            # remove any numbers
            text = ''.join([i for i in text if not i.isdigit()])
            # replace dash and spaces with comma for later splitting
            text = text.replace('-', ',').strip()

        if scrub_names:
            text = text.strip()
            if len(text) > 1:
                return text

        else:
            return text

# Executes the script
if __name__ == "__main__":
    get_article_text()
    #shuffle_article_text()
