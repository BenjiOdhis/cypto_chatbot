# CryptoBuddy: My First AI-Powered Financial Sidekick! 🌟

# Step 1: Define the crypto database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}

# Step 2: Define the chatbot's personality
def welcome():
    print("👋 Hey there! I'm CryptoBuddy — your AI-powered crypto sidekick.")
    print("Ask me anything like:")
    print("• Which crypto is trending up?")
    print("• What’s the most sustainable coin?")
    print("• Which crypto should I buy for long-term growth?")
    print("⚠️ Disclaimer: Crypto is risky—always do your own research!\n")

# Step 3: Define the chatbot logic
def get_response(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 {recommend} is the most eco-friendly with a sustainability score of {crypto_db[recommend]['sustainability_score']*10}/10."

    elif "trending" in user_query or "rising" in user_query:
        trending_cryptos = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 These cryptos are trending up: {', '.join(trending_cryptos)}."

    elif "long-term" in user_query or "growth" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f"🚀 {name} is trending and has strong sustainability. Great for long-term growth!"

        return "🤔 Hmm, nothing fits that perfectly right now. Try again soon!"

    elif "advice" in user_query or "recommend" in user_query or "buy" in user_query:
        best = None
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                best = name
                break
        if best:
            return f"💡 I recommend {best} — strong market cap and rising prices!"
        else:
            return "📉 Nothing strong to recommend right now."

    else:
        return "❓ I'm not sure how to answer that. Try asking about trends, sustainability, or long-term growth!"

# Step 4: Run the chatbot loop
def run_chatbot():
    welcome()
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit", "bye"]:
            print("CryptoBuddy: 👋 Goodbye! Stay safe and keep learning about crypto!")
            break
        response = get_response(query)
        print(f"CryptoBuddy: {response}")

run_chatbot()
