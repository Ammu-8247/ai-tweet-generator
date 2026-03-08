import random

def analyze_brand_voice(brand_name, industry, objective, products):
    # Mock analysis based on inputs
    tone = "witty" if "fun" in products.lower() or "meme" in objective.lower() else "professional"
    audience = "young adults" if "engagement" in objective.lower() else "general consumers"
    themes = "promotional and informative" if "promotion" in objective.lower() else "educational and community-focused"
    return [
        f"Tone: {tone}",
        f"Target audience: {audience}",
        f"Content themes: {themes}"
    ]

def generate_tweets(voice_summary, brand_name, objective, products):
    # Mock tweets based on brand
    base_tweets = [
        f"Excited to share our latest {products.split()[0]}! Check it out. #{brand_name}",
        f"What's your favorite way to use {products}? Tell us! 💬",
        f"Pro tip: {products} can change your day. Try it! 🌟",
        f"Join the {brand_name} community. We're all about {objective}.",
        f"Meme time: When {products} saves the day! 😂",
        f"Learn more about {products} and why it matters.",
        f"Promotion alert: Special offer on {products} now!",
        f"Behind the scenes at {brand_name}: Crafting {products}.",
        f"Did you know? {products} is designed for {objective}.",
        f"Share your story with {brand_name}. We love hearing from you!"
    ]
    random.shuffle(base_tweets)
    return base_tweets[:10]

def main():
    print("AI Tweet Generator")
    brand_name = input("Brand Name (Optional): ")
    industry = input("Industry / Category (Optional): ")
    objective = input("Campaign Objective (e.g., engagement, promotion, awareness): ")
    products = input("More about the brand's products: ")

    voice_summary = analyze_brand_voice(brand_name, industry, objective, products)
    tweets = generate_tweets(voice_summary, brand_name, objective, products)

    print("\nBrand Voice Summary:")
    for point in voice_summary:
        print(f"- {point}")

    print("\nGenerated Tweets:")
    for i, tweet in enumerate(tweets, 1):
        print(f"{i}. {tweet}")

if __name__ == '__main__':
    main()
