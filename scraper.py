import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from database import engine
from models import Book, Category
import re


BASE_URL = "https://books.toscrape.com/"

def get_categories():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    
    categories = {}
    for category in soup.select(".side_categories ul li ul li a"):
        name = category.text.strip()
        url = BASE_URL + category["href"]
        categories[name] = url
    
    return categories

def scrape_books(category_name, category_url, db: Session):
    page=1
    while True:
        url = category_url.replace("index.html", f"page-{page}.html")
        response = requests.get(url, headers={"Accept-Charset": "utf-8"})
        response.encoding = 'utf-8'
        if response.status_code != 200:
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.select(".product_pod")
        
        if not books:
            break
        
        for book in books:
            title = book.h3.a["title"]
            price_text = book.select_one(".price_color").text.strip()
            price_cleaned = re.sub(r"[^\d.]", "", price_text)  # Supprime tous les caractères sauf les chiffres et "."
            price = float(price_cleaned)
            rating = convert_rating(book.select_one(".star-rating")["class"][1])
            availability = book.select_one(".instock.availability").text.strip()
            book_url = BASE_URL + book.h3.a["href"]
        
            category = db.query(Category).filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
                db.add(category)
                db.commit()

            existing_book = db.query(Book).filter_by(url=book_url).first()
            if not existing_book:
                new_book = Book(
                    title=title,
                    price=price,
                    rating=rating,
                    availability=availability,
                    url=book_url,
                    category_id=category.id
                )
                db.add(new_book)
                db.commit()
        
        page += 1

def convert_rating(rating_text):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(rating_text, 0)

def main():
    
    db = Session(engine)
    categories = get_categories()
    
    for name in categories.keys():
        existing_category = db.query(Category).filter_by(name=name).first()
        if not existing_category:
            new_category = (Category(name=name))
            db.add(new_category)
    
    db.commit()
    
    for name, url in categories.items():
        print(f"Scraping catégorie : {name}")
        scrape_books(name, url, db)
    
    db.close()
    print("✅ Scraping terminé avec succès !")
    

if __name__ == "__main__":
    main()
    