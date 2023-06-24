import requests
from bs4 import BeautifulSoup

# Make a request to the website
response = requests.get("https://trends24.in/indonesia/")

# Create BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Find the trending topics container
trends_container = soup.find("ol", class_="trend-card__list")

# Find all the list items within the container
trends_items = trends_container.find_all("li")

# Display the trending topics
print("Current Viral Trends in Indonesia:")
for item in trends_items:
    topic = item.a.text.strip()
    tweet_count = item.find("span", class_="tweet-count")
    if tweet_count:
        tweet_count = tweet_count.text.strip()
    else:
        tweet_count = "N/A"
    print(f"{topic} - {tweet_count}")
