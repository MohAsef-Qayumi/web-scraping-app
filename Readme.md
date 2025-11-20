# 📚 Books Scraper (Python + BeautifulSoup)

A simple and clean web-scraping project that extracts book information from  
**https://books.toscrape.com/** — a website intentionally made for scraping practice.

This scraper automatically navigates through **all pages**, collects book details, and saves them into a CSV file.

---

## 🚀 Features

- Scrapes all books across multiple pages
- Extracts:
  - **Title**
  - **Price**
  - **Availability**
- Saves the output to **books.csv**
- Uses `requests` and `BeautifulSoup`
- Fully open-source and easy to modify

---

## 📂 Project Structure

books_scraper/
│
└── scraper/
├── requirements.txt
└── main.py

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/books_scraper.git
   cd books_scraper
2. Install dependencies
    ```bash
    pip install -r requirements.txt
3. (Optional but recommended) Create a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate      # macOS/Linux
    venv\Scripts\activate         # Windows

## ▶️ Running the Scraper

From the project root:
    ```bash
    python scraper/main.py

## This will:
    1. Start scraping all pages
    2.  Print progress in the terminal
    3.  Generate a file named books.csv in the project root

## 🧪 Output Example (books.csv)

    title,price,availability
    "A Light in the Attic","£51.77","In stock"
    "Tipping the Velvet","£53.74","In stock"
    

## ⚙️ How It Works

Requests the first page in /catalogue

Finds the Next button on each page

Automatically moves to the next page until none exists

Parses the HTML using BeautifulSoup

Collects book information and stores it in a list

Writes all results to a CSV file


## 🧩 Technologies Used

Python 3

requests

beautifulsoup4

CSV module

## 🤝 Contributing

Pull requests are welcome!
If you’d like to improve pagination, add JSON output, or implement async scraping, feel free to contribute.