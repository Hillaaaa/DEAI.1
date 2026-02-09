def text_analyser(text):

    normalized_text = text.lower()
    words = normalized_text.split()
    total_words = len(words)
    total_characters = len(normalized_text)
    longest_word =""
    word_frequency = {}
    total_length = 0
    for word in words:
        total_length += len(word)
        if len(word) > len(longest_word):
            longest_word = word
        word_frequency[word] = word_frequency.get(word,0)+1
    max_count = 0
    frequent_word = ""
    for word , count in word_frequency.items():
        if count > max_count:
            max_count = count
            frequent_word = word
    if total_words > 0:
        average_word_length = total_length/total_words
    else:
        average_word_length = 0

    return {
        "features":{
        "words":total_words,
        "characters":total_characters,
        "word_frequency":word_frequency,
        "longest_word": longest_word,
        "frequent_word": frequent_word,
        "average_word_length": average_word_length}
    }

