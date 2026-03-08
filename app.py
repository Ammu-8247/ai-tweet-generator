from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Tweet Generator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 700px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 1.1em;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            color: #333;
            font-weight: bold;
            margin-top: 15px;
            margin-bottom: 8px;
            font-size: 1.05em;
        }
        input[type="text"], textarea {
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1em;
            transition: border-color 0.3s;
        }
        input[type="text"]:focus, textarea:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
        }
        textarea {
            resize: vertical;
            min-height: 100px;
        }
        input[type="submit"] {
            margin-top: 25px;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        input[type="submit"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }
        .results {
            margin-top: 40px;
            padding-top: 30px;
            border-top: 3px solid #667eea;
        }
        h2 {
            color: #667eea;
            margin-top: 25px;
            margin-bottom: 15px;
            font-size: 1.5em;
        }
        ul, ol {
            margin-left: 20px;
        }
        li {
            margin: 12px 0;
            line-height: 1.6;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 AI Tweet Generator 🚀</h1>
        <p class="subtitle">✨ Create engaging tweets for your brand ✨</p>
        <form method="POST">
            <label>📝 Brand Name (Optional):</label>
            <input type="text" name="brand_name" placeholder="e.g., Nike, Starbucks, Tesla"><br>
            <label>🏢 Industry / Category (Optional):</label>
            <input type="text" name="industry" placeholder="e.g., Fashion, Tech, Food & Beverage"><br>
            <label>🎯 Campaign Objective (e.g., engagement, promotion, awareness):</label>
            <input type="text" name="objective" placeholder="What do you want to achieve?"><br>
            <label>📦 Tell us about the brand's products:</label>
            <textarea name="products" placeholder="Describe your products or services..."></textarea><br>
            <input type="submit" value="✨ Generate Tweets ✨">
        </form>
        {% if result %}
        <div class="results">
            <h2>🎤 Brand Voice Summary:</h2>
            <ul>
                {% for point in result.voice_summary %}
                <li>{{ point }}</li>
                {% endfor %}
            </ul>
            <h2>💬 Generated Tweets:</h2>
            <ol>
                {% for tweet in result.tweets %}
                <li>{{ tweet }}</li>
                {% endfor %}
            </ol>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

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

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        brand_name = request.form.get('brand_name', 'Brand')
        industry = request.form.get('industry', 'General')
        objective = request.form.get('objective', 'engagement')
        products = request.form.get('products', 'products')

        voice_summary = analyze_brand_voice(brand_name, industry, objective, products)
        tweets = generate_tweets(voice_summary, brand_name, objective, products)
        result = {'voice_summary': voice_summary, 'tweets': tweets}

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
