from textblob import TextBlob

text = input("Enter a sentence: ")
result = TextBlob(text).sentiment.polarity
if result > 0:
    print("Positive")
elif result < 0:
    print("Negative")
else:
    print("Neutral")
