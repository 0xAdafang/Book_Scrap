import csv
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Book, Category

def get_books_filtered(category=None, min_rating=None, min_price=None, max_price=None):
    db = SessionLocal()
    
    query = db.query(Book.title, Book.price, Book.rating, Category.name).join(Category)
    
    if category:
        query = query.filter(Category.name == category)
    if min_rating:
        query = query.filter(Book.rating >= min_rating)
    if min_price:
        query = query.filter(Book.price >= min_price)
    if max_price:
        query = query.filter(Book.price <= max_price)
    
    books = query.all()
    db.close()
   
    return books

def get_all_categories():
    
    db = SessionLocal()
    categories = db.query(Category.name).all()
    db.close()

    return [category[0] for category in categories]

def export_books_to_csv(filename="books.csv", category=None, min_rating=None, min_price=None, max_price=None):
    books = get_books_filtered(category, min_rating, min_price, max_price)
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price (£)", "Rating", "Category"])
        for title, price, rating, category, in books:
            writer.writerow([title, price, rating, category])
    
    print(f"✅ Export terminé : {filename}")
    

if __name__ == "__main__":
    
    export_books_to_csv()
    
    
    
        
        