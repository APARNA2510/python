
def vowel_counter(sentence):
    result = {}            # create a dictionary

    for vowel in "aeiou":  # loop through the vowel
        result[vowel] = sentence.lower().count(vowel)
    return result

if __name__ == "__main__":
    msg = "This is a test"
    print(vowel_counter(msg))        
    