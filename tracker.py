import json
import os

# File to store the books
FILE = 'tbr.json'

# Load existing books
def load_books():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return []

# Save books to file
def save_books(books):
    with open(FILE, 'w') as f:
        json.dump(books, f, indent=4)

# Add a new book
def add_book():
    title = input("📖 Enter book title: ")
    author = input("👤 Enter author name: ")
    genre = input("🎯 Genre: ")
    status = input("📌 Status (Want to Read / Reading / Completed): ")

    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "status": status,
        "review": "",
        "rating": None
    }

    books = load_books()
    books.append(book)
    save_books(books)
    print(f"\n✅ '{title}' added to your TBR list!")

# List books (optionally filter by status)
def list_books(filter_status=None):
    books = load_books()
    if filter_status:
        books = [b for b in books if b['status'].lower() == filter_status.lower()]
    
    if not books:
        print("⚠️ No books found.")
        return
    
    for idx, book in enumerate(books, 1):
        print(f"\n📚 {idx}. {book['title']} by {book['author']}")
        print(f"   Genre: {book['genre']} | Status: {book['status']}")
        if book["review"]:
            print(f"   ✍️  Review: {book['review']} | ⭐ Rating: {book['rating']}")

# Update book status/review
def update_book():
    books = load_books()
    if not books:
        print("⚠️ No books to update.")
        return

    list_books()
    try:
        index = int(input("\nEnter book number to update: ")) - 1
        if 0 <= index < len(books):
            books[index]["status"] = input("📌 New status: ")
            books[index]["review"] = input("✍️ Review (optional): ")
            rating_input = input("⭐ Rating out of 5 (optional): ")
            if rating_input.strip():
                books[index]["rating"] = float(rating_input)
            save_books(books)
            print("✅ Book updated!")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Enter a valid number.")

# Main menu loop
def menu():
    while True:
        print("\n📚 TBR Tracker Menu:")
        print("1. Add Book")
        print("2. View All Books")
        print("3. View Books by Status")
        print("4. Update Book")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            status = input("Enter status (Want to Read / Reading / Completed): ")
            list_books(status)
        elif choice == "4":
            update_book()
        elif choice == "5":
            print("👋 Bye! Keep reading.")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the menu
menu()
