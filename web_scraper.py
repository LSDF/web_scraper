import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Scraping article titles and links
    data = []
    for article in soup.find_all('h2'):
        title = article.get_text()
        link = article.find('a')['href']
        data.append({'title': title, 'link': link})

    return data

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    url = ''  # Replace with the URL you want to scrape
    data = scrape_website(url)
    save_to_csv(data, 'scraped_data.csv')
    print("Data has been scraped and saved to scraped_data.csv")
