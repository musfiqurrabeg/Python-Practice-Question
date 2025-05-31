def count_word_frequency(sentence):
    words = sentence.lower().split()
    
    # Initialize an empty dictionary to store word frequencies
    frequency_dict = {}
    
    # Count frequency of each word
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    
    return frequency_dict
