import random

# article_text = original parsed article text file
# shuffled_text = file where we will write the shuffled text
def shuffle_article_text(
    article_text="data/microwave_limb_sounder/article_text.jsonl",
    shuffled_text="data/microwave_limb_sounder/shuffle_text.jsonl",
    training_set="data/microwave_limb_sounder/training_set.jsonl",
    validation_set="data/microwave_limb_sounder/validation_set.jsonl",
    test_set="data/microwave_limb_sounder/test_set.jsonl"
):

    # Open the original file and randomize the order
    with open(article_text,'r') as source:
        data = [(random.random(), line) for line in source]
        source.close()
    
    # Sorts the data (not entirely sure why this works, but hey)
    data.sort()

    # Writes 70% of shuffled text to training set
    with open(training_set,'w+') as target:
        for i,line in data:
            if i > len(data)*0.7:
                print("Test")
                print(i)
                break
            target.write(line)
    target.close()

    # Writes 15% of shuffled text to training set
    # with open(validation_set,'w+') as target:
    #     for i,line in data:
    #         if i > len(data)*0.7 and i < len(data)*0.85:
    #             target.write(line)
    #         else:
    #             break
    # target.close()

    # # Writes 15% of shuffled text to training set
    # with open(test_set,'w+') as target:
    #     for i,line in data:
    #         if i >= len(data)*0.85:
    #             break
    #         target.write(line)
    # target.close()

# Executes the script
if __name__ == "__main__":
    shuffle_article_text()
