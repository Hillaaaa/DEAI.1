def spam_detector(message):
    spam_words = {"win", "free", "prize", "money"}

    message = message.lower()
    words = message.split()

    for word in words:
        if word in spam_words:
            return "This is spam"

    return "This is safe"


message = input("Enter your message: ")
result = spam_detector(message)
print(result)
