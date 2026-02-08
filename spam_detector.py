def spam_detector(message):
    spam_words = {"win", "prize", "free", "money"}
    message = message.lower()
    words = message.split()
    is_spam = False
    for word in words:
        if word in spam_words:
            is_spam = True
            break
    if is_spam:
        return "This is spam"
    else:
        return "This is safe"

message = input("Enter your message: ")
print(spam_detector(message))