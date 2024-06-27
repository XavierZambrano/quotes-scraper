import requests
from bs4 import BeautifulSoup
import json

def get_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        
        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })
    
    return json.dumps(quotes)

if __name__ == "__main__":
    quotes = get_quotes()
    print(quotes)