import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://books.toscrape.com/"

def scrape_page(url):
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    books = []
    for article in soup.select(".product_pod"):
        title = article.h3.a["title"]
        price = article.select_one(".price_color").text.strip()
        availability = article.select_one(".availability").text.strip()
        books.append({
            "title": title,
            "price": price,
            "availability": availability
        })
    return books, soup

def scrape_all():
    url = BASE_URL + "catalogue/page-1.html"
    all_books = []

    while url:
        print(f"Scraping: {url}")
        books, soup = scrape_page(url)
        all_books.extend(books)

        next_btn = soup.select_one("li.next > a")
        if next_btn:
            # Fix: catalogue/ must be included for all pages
            url = BASE_URL + "catalogue/" + next_btn["href"]
        else:
            url = None

    with open("books.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "availability"])
        writer.writeheader()
        writer.writerows(all_books)

    print(f"Saved {len(all_books)} books to books.csv")

if __name__ == "__main__":
    scrape_all()
