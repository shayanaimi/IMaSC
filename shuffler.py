import random

# article_text is the original parsed article text file
# The sets are my training, validation, and testing sets for Prodigy
def shuffle_article_text(
    article_text="data/microwave_limb_sounder/article_text.jsonl",
    training_set_1="data/microwave_limb_sounder/training_set_1.jsonl",
    training_set_2="data/microwave_limb_sounder/training_set_2.jsonl",
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
    training_1 = open(training_set_1, "w+")
    training_2 = open(training_set_2, "w+")
    validation = open(validation_set, "w+")
    testing = open(testing_set, "w+")

    for j in range(len(data)):

        if j < len(data)*0.35:
            training_1.write(data[j][1])
        elif j >= len(data)*0.35 and j < len(data)*0.7:
            training_2.write(data[j][1])
        elif j >= len(data)*0.7 and j < len(data)*0.85:
            validation.write(data[j][1])
        else:
            testing.write(data[j][1])  
        
    training_1.close()
    training_2.close()
    validation.close()
    testing.close()

# Executes the script
if __name__ == "__main__":
    shuffle_article_text()
