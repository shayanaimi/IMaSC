import random

# article_text = original parsed article text file
# shuffled_text = file where we will write the shuffled text
def shuffle_article_text(
    article_text="data/microwave_limb_sounder/article_text.jsonl",
    shuffled_text="data/microwave_limb_sounder/shuffle_text.jsonl"
):

    # Open the original file and randomize the order
    with open(article_text,'r') as source:
        data = [(random.random(), line) for line in source]
        source.close()
    
    #
    data.sort()

    with open(shuffled_text,'w+') as target:
        for _, line in data:
            target.write(line)
        target.close()

# Executes the script
if __name__ == "__main__":
    shuffle_article_text()
