# <!-- 0781f26847284dd08122936a7055ebfd -->
# https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY


import requests

API_KEY = "0781f26847284dd08122936a7055ebfd"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

params = {
    "country": "us", #US news
    "category": "technology",
    "pageSize": 5, # limit reults
    "apiKey": API_KEY
}

# Make the request
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    articles = data.get("articles", [])

    for i, article in enumerate(articles, start=1):
        print(f"{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Published At: {article['publishedAt']}")
        print(f"   URL: {article['url']}\n")
else:
    print(f"Failed to retrieve news: {response.status_code}")
    print(response.text)