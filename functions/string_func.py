from string import punctuation

def remove_punc(text):
    '''
    Remove punctuation from a text and return cleaned text

    'clean_text = remove_punc(text)'
    '''
    for punc in punctuation:
        text  = text.replace(punc, '')
    return text 

def word_count(text):
    wordlist = text.lower().split()
    wc ={}
    for word in wordlist:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 
    return wc

def sort(word_dict):
    ans = sorted(word_dict.items(),key=lambda val: val[1], reverse= True)
    return dict(ans)    

if __name__ == '__main__':
    long_text = ''' 
    The quic brown fox jumps over the lazy dog,
    and attacks the chicken with a flying kick.
    This is real life story about a fox, that could
    kick and jump. If you are really interested in 
    this story, then keep reading. The End.
    '''

    cl_text = remove_punc(long_text)
    counted_word = word_count(cl_text)
    sorted_words = sort(counted_word)
    print(sorted_words)            