from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.1:
        return "Positive", polarity
    elif polarity < -0.1:
        return "Negative", polarity
    else:
        return "Neutral", polarity

while True:
    print("\n=== Sentiment Analysis ===")
    print("1. Analyze text")
    print("2. Exit")
    
    choice = input("\nEnter choice (1/2): ")
    
    if choice == "1":
        text = input("Enter text to analyze: ")
        sentiment, score = analyze_sentiment(text)
        print(f"\nSentiment: {sentiment}")
        print(f"Score: {score:.2f}")
        
    elif choice == "2":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
