def spam_detector(message):
    spam_words = {"win", "free", "prize", "money"}

    message = message.lower()
    words = message.split()

    for word in words:
        if word in spam_words:
            return {
                "result": "spam",
                "matched_word": word,
            }

    return {
        'result': "safe",
        'matched_word': None
    }


message = input("Enter your message: ")
result = spam_detector(message)
print(result)
