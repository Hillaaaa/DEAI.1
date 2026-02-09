def text_analyser(text):

    normalized_text = text.lower()
    words = normalized_text.split()
    total_words = len(words)
    total_characters = len(normalized_text)
    longest_word =""
    word_frequency = {}


    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
        word_frequency[word] = word_frequency.get(word,0)+1


    return {
        "words":total_words,
        "characters":total_characters,
        "word_frequency":word_frequency,
        "longest_word": longest_word,
    }
